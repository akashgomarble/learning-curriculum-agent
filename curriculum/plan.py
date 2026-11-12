"""Stage 1: turn the learner profile into ordered sub-topics, search queries and exclusion rules."""

from .llm import Ledger, chat_json
from .models import Persona, PlanOut
from .prompts import load, persona_block


def make_plan(persona: Persona, ledger: Ledger, model: str) -> PlanOut:
    plan = chat_json(model, load("plan"), persona_block(persona), PlanOut, stage="plan", ledger=ledger, max_tokens=8000)
    plan.search_queries = [q for q in plan.search_queries if q.strip()][:7]
    plan.title_exclusions = [t.lower().strip() for t in plan.title_exclusions if t.strip()]
    return plan
