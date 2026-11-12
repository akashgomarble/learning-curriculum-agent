"""LLM client (OpenRouter): one function, `chat_json`,
that returns a validated pydantic object.

Every call asks for a strict JSON schema, validates the reply with pydantic, retries once with the
validation error if the reply is malformed, and records cost/latency in a ledger.
"""

from __future__ import annotations

import copy
import json
import os
import threading
from types import SimpleNamespace
import time
from dataclasses import dataclass, field
from typing import TypeVar

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, ValidationError

load_dotenv()

T = TypeVar("T", bound=BaseModel)

# Keywords some providers reject in strict mode; pydantic still enforces what matters after the call.
_UNSUPPORTED = {"default", "minimum", "maximum", "minItems", "maxItems", "minLength", "maxLength", "pattern", "format"}


class BudgetExceeded(RuntimeError):
    pass


@dataclass
class Call:
    stage: str
    model: str
    prompt_tokens: int
    completion_tokens: int
    cost_usd: float
    latency_s: float


@dataclass
class Ledger:
    """Collects cost and latency of every LLM call in a run. Thread-safe.

    Uncapped by default; set MAX_RUN_USD (or pass max_usd>0) to abort a run past a dollar ceiling."""

    max_usd: float = float(os.getenv("MAX_RUN_USD", "0"))  # 0 = no cap
    calls: list[Call] = field(default_factory=list)
    _lock: threading.Lock = field(default_factory=threading.Lock, repr=False)

    def add(self, call: Call) -> None:
        with self._lock:
            self.calls.append(call)
            if self.max_usd and self.total_cost > self.max_usd:
                raise BudgetExceeded(f"run cost ${self.total_cost:.3f} > MAX_RUN_USD ${self.max_usd}")

    @property
    def total_cost(self) -> float:
        return round(sum(c.cost_usd for c in self.calls), 5)

    def by_stage(self) -> dict[str, dict]:
        out: dict[str, dict] = {}
        for c in self.calls:
            s = out.setdefault(c.stage, {"calls": 0, "cost_usd": 0.0, "prompt_tokens": 0, "completion_tokens": 0, "latency_s": 0.0})
            s["calls"] += 1
            s["cost_usd"] = round(s["cost_usd"] + c.cost_usd, 5)
            s["prompt_tokens"] += c.prompt_tokens
            s["completion_tokens"] += c.completion_tokens
            s["latency_s"] = round(s["latency_s"] + c.latency_s, 2)
        return out


_client: OpenAI | None = None


def client() -> OpenAI:
    global _client
    if _client is None:
        key = os.getenv("OPENROUTER_API_KEY")
        if not key:
            raise SystemExit("OPENROUTER_API_KEY is not set (copy .env.example to .env).")
        _client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=key, timeout=180, max_retries=3)
    return _client


def strict_schema(model: type[BaseModel]) -> dict:
    """pydantic schema -> strict JSON schema: refs inlined, every property required, no extra keys."""
    schema = model.model_json_schema()
    defs = schema.pop("$defs", {})

    def walk(node, prop_map: bool = False):
        if isinstance(node, dict):
            if prop_map:  # keys here are property NAMES (a field may be called "default" or "title"), never keywords
                return {k: walk(v) for k, v in node.items()}
            if "$ref" in node:
                return walk(copy.deepcopy(defs[node["$ref"].split("/")[-1]]))
            node = {k: walk(v, prop_map=(k == "properties")) for k, v in node.items()
                    if k not in _UNSUPPORTED and k != "title"}
            if node.get("type") == "object" and "properties" in node:
                node["required"] = list(node["properties"])
                node["additionalProperties"] = False
            if "prefixItems" in node:  # tuples -> plain arrays
                node["items"] = node.pop("prefixItems")[0]
            return node
        if isinstance(node, list):
            return [walk(v) for v in node]
        return node

    return walk(schema)


def chat_json(
    model: str,
    system: str,
    user: str,
    schema: type[T],
    *,
    stage: str,
    ledger: Ledger | None = None,
    max_tokens: int = 4000,
) -> T:
    messages = [{"role": "system", "content": system}, {"role": "user", "content": user}]
    response_format = {
        "type": "json_schema",
        "json_schema": {"name": schema.__name__, "strict": True, "schema": strict_schema(schema)},
    }
    last_err = None
    for attempt in range(2):
        t0 = time.time()
        extra = {"provider": {"require_parameters": True}, "usage": {"include": True}}
        resp = client().chat.completions.create(
            model=model,
            messages=messages,
            response_format=response_format,
            max_tokens=max_tokens,
            extra_body=extra,
        )
        latency = time.time() - t0
        usage = resp.usage.model_dump() if resp.usage else {}
        if ledger is not None:
            ledger.add(
                Call(
                    stage=stage,
                    model=model,
                    prompt_tokens=usage.get("prompt_tokens") or 0,
                    completion_tokens=usage.get("completion_tokens") or 0,
                    cost_usd=float(usage.get("cost") or usage.get("estimated_cost") or 0.0),
                    latency_s=round(latency, 2),
                )
            )
        text = (resp.choices[0].message.content or "").strip()
        if resp.choices[0].finish_reason == "length":  # reasoning + answer ran out of room: retry with more
            max_tokens *= 2
            last_err = RuntimeError("reply truncated (finish_reason=length)")
            continue
        try:
            return schema.model_validate(json.loads(_strip_fences(text)))
        except (json.JSONDecodeError, ValidationError) as e:
            last_err = e
            messages += [
                {"role": "assistant", "content": text},
                {"role": "user", "content": f"That reply did not match the schema: {str(e)[:800]}. Reply again with valid JSON only."},
            ]
    raise RuntimeError(f"{stage}: model {model} returned invalid JSON twice: {last_err}")


def chat_tools(model: str, messages: list[dict], tools: list[dict], *, stage: str, ledger: Ledger | None = None,
               max_tokens: int = 4000, tool_choice: str = "auto", on_token=None):
    """One turn of a tool-using agent loop: send the running message list plus the tool schemas, return the
    assistant message (which may carry tool_calls). The caller executes the tools, appends the results, and
    calls again. Cost/latency go to the ledger exactly like chat_json, so both architectures are priced the same.

    When `on_token` is given, the reply is streamed and each text delta is handed to it (for the live chat UI);
    otherwise a single non-streamed call is made (the CLI and the eval, so their cost accounting stays exact)."""
    t0 = time.time()
    extra = {"provider": {"require_parameters": True}, "usage": {"include": True}}
    if on_token is None:
        resp = client().chat.completions.create(
            model=model, messages=messages, tools=tools, tool_choice=tool_choice,
            max_tokens=max_tokens, extra_body=extra,
        )
        usage = resp.usage.model_dump() if resp.usage else {}
        _bill(ledger, stage, model, usage, t0)
        return resp.choices[0].message
    # streaming path: accumulate text (streamed to on_token) and tool-call deltas, then rebuild a message
    stream = client().chat.completions.create(
        model=model, messages=messages, tools=tools, tool_choice=tool_choice, max_tokens=max_tokens,
        stream=True, stream_options={"include_usage": True}, extra_body=extra,
    )
    content, tcs, usage = [], {}, {}
    for chunk in stream:
        if getattr(chunk, "usage", None):
            usage = chunk.usage.model_dump()
        if not chunk.choices:
            continue
        d = chunk.choices[0].delta
        if getattr(d, "content", None):
            content.append(d.content)
            on_token(d.content)
        for td in (getattr(d, "tool_calls", None) or []):
            slot = tcs.setdefault(td.index, {"id": None, "name": "", "args": ""})
            if td.id:
                slot["id"] = td.id
            if td.function and td.function.name:
                slot["name"] += td.function.name
            if td.function and td.function.arguments:
                slot["args"] += td.function.arguments
    _bill(ledger, stage, model, usage, t0)
    calls = [SimpleNamespace(id=v["id"] or f"call_{i}", type="function",
                             function=SimpleNamespace(name=v["name"], arguments=v["args"]))
             for i, (_, v) in enumerate(sorted(tcs.items()))]
    return SimpleNamespace(content="".join(content), tool_calls=calls or None)


def _bill(ledger, stage, model, usage, t0):
    if ledger is not None:
        ledger.add(Call(stage=stage, model=model, prompt_tokens=usage.get("prompt_tokens") or 0,
                        completion_tokens=usage.get("completion_tokens") or 0,
                        cost_usd=float(usage.get("cost") or usage.get("estimated_cost") or 0.0),
                        latency_s=round(time.time() - t0, 2)))


def _strip_fences(text: str) -> str:
    if text.startswith("```"):
        text = text.split("\n", 1)[1] if "\n" in text else text
        text = text.rsplit("```", 1)[0]
    return text
