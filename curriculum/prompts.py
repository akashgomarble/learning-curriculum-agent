from functools import cache
from pathlib import Path

from .models import Persona

_DIR = Path(__file__).parent / "prompts"


@cache
def load(name: str) -> str:
    return (_DIR / f"{name}.md").read_text()


def persona_block(p: Persona) -> str:
    c = p.user_context
    return (
        f"Goal: {p.goal}\n"
        f"Time budget: {p.time_budget_minutes} minutes\n"
        f"Background: {c.background or '-'}\n"
        f"Already knows: {', '.join(c.known) or '-'}\n"
        f"Does not know yet: {', '.join(c.unknown) or '-'}\n"
        f"Constraints: {c.constraints or '-'}"
    )
