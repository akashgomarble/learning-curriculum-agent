"""Data shapes used across the pipeline.

Two kinds of models live here:
- *Domain* models (Persona, Candidate, Curriculum, ...) that the code builds and saves.
- *LLM output* models (PlanOut, AssessOut, SelectOut) that define the JSON each LLM call must return.
  They are kept flat and small on purpose: the LLM decides, the code assembles and checks.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

# ---------------------------------------------------------------- inputs


class UserContext(BaseModel):
    background: str = ""
    known: list[str] = []
    unknown: list[str] = []
    constraints: str = ""


class Expectations(BaseModel):
    """What 'good' means for a test persona, written before any run. Read only by the eval."""

    pick_count: tuple[int, int] = (3, 8)
    min_utilisation: float = 0.6
    max_utilisation: float = 1.0
    forbidden_title_regex: str | None = None
    forbidden_flags: list[str] = []
    # Each entry is one 'unknown' item and the words that count as covering it.
    unknown_synonyms: dict[str, list[str]] = {}
    known_topics: list[str] = []
    min_level: Literal["beginner", "intermediate", "advanced"] | None = None
    require_project_based: bool = False
    required_language: str | None = None
    expect_infeasible: bool = False
    expect_assumptions: bool = False
    min_upload_year: int | None = None  # tools changed: nothing older than this
    max_sitting_minutes: float | None = None  # no single pick (or slice) longer than this
    max_channels: int | None = None  # follow at most N creators
    max_per_channel: int | None = None  # at most N picks from one creator
    notes: str = ""


class Persona(BaseModel):
    persona_id: str
    goal: str
    time_budget_minutes: int
    user_context: UserContext = UserContext()
    expectations: Expectations | None = None


# ---------------------------------------------------------------- YouTube


class Snippet(BaseModel):
    start: float
    text: str


class Candidate(BaseModel):
    video_id: str
    title: str
    channel: str = ""
    duration_s: int = 0
    view_count: int | None = None
    description: str = ""
    found_by: list[str] = []  # queries that surfaced it
    transcript_lang: str | None = None
    transcript_generated: bool | None = None
    transcript_error: str | None = None
    upload_date: str | None = None
    chapters: list[dict] = []
    evidence_kind: Literal["transcript", "metadata", "none"] = "none"
    windows: str = ""  # the time-stamped evidence text the assessor reads (transcript excerpt, or chapters+description)

    @property
    def url(self) -> str:
        return f"https://www.youtube.com/watch?v={self.video_id}"

    @property
    def minutes(self) -> float:
        return round(self.duration_s / 60, 1)


# ---------------------------------------------------------------- stage 1: plan

Level = Literal["beginner", "intermediate", "advanced"]


class SubTopic(BaseModel):
    id: str = Field(description="short snake_case id, e.g. vite_setup")
    title: str
    why: str = Field(description="why this learner needs it, given what they already know")
    prereqs: list[str] = Field(description="ids of sub-topics that must come before this one")
    minutes_share: float = Field(description="rough share of the budget, 0-1")


class PlanOut(BaseModel):
    interpretation: str = Field(description="one sentence: what success looks like for this learner")
    assumptions: list[str] = Field(description="assumptions made because the goal or context is ambiguous; empty if none")
    feasible: bool = Field(description="can the goal realistically be met within the budget?")
    feasibility_note: str = Field(description="if not feasible, what part of the goal is realistic; else empty")
    preferred_language: str = Field(description="ISO 639-1 code of the language videos should be in, e.g. en")
    learner_level: Level
    sub_topics: list[SubTopic]
    search_queries: list[str] = Field(description="5-7 YouTube search queries")
    title_exclusions: list[str] = Field(
        description="lower-case phrases that, if present in a title, rule the video out (from the constraints)"
    )
    skip_topics: list[str] = Field(description="topics the learner already knows and should not be re-taught")


# ---------------------------------------------------------------- stage 4: assess

RedFlag = Literal[
    "surface_intro",
    "pure_theory",
    "outdated_tooling",
    "wrong_language",
    "off_topic",
    "clickbait",
    "vlog",
    "equipment_review",
    "too_basic_for_learner",
    "too_advanced_for_learner",
    "poor_transcript",
]


class Quote(BaseModel):
    id: str = Field(description="q1, q2, ...")
    t: int = Field(description="timestamp in seconds where the quote is said")
    text: str = Field(description="verbatim words copied from the transcript, 6-30 words")


class Segment(BaseModel):
    start_s: int
    end_s: int
    topic: str


class Relevance(BaseModel):
    sub_topic_id: str
    score: int = Field(description="0 = not covered, 1 = mentioned, 2 = taught, 3 = taught hands-on in depth")


class AssessOut(BaseModel):
    spoken_language: str = Field(description="ISO 639-1 code of the language actually spoken")
    summary: str = Field(description="2-3 sentences on what is actually taught or built, from the transcript")
    topics_covered: list[str] = Field(description="3-10 short lower-case topic labels, e.g. 'usestate', 'localstorage'")
    level: Level
    format: Literal["project_build", "concept_explainer", "lecture", "full_course", "crash_course", "vlog", "review", "other"]
    is_project_based: bool
    project_built: str = Field(description="what gets built, if anything; empty if nothing")
    tools_and_versions: list[str] = Field(description="tools, libraries and versions mentioned, e.g. 'vite', 'react 19'")
    red_flags: list[RedFlag]
    quotes: list[Quote] = Field(description="2-4 verbatim quotes that show what is taught")
    segments: list[Segment] = Field(description="rough map of what happens when, from the timestamps you can see")
    relevance: list[Relevance] = Field(description="one entry per sub-topic of the plan")


class Assessment(AssessOut):
    """AssessOut plus what the code adds after checking it."""

    video_id: str
    evidence_source: Literal["transcript", "metadata"] = "transcript"
    verified_quote_ids: list[str] = []


# ---------------------------------------------------------------- stage 6: select


class PickOut(BaseModel):
    video_id: str
    covers: list[str] = Field(description="sub-topic ids this pick covers")
    reason: str = Field(description="1-3 sentences on why this video, for this learner, citing what it teaches")
    evidence_quote_ids: list[str] = Field(description="ids of verified quotes that back the reason")
    watch_from_s: int | None = Field(description="start second if only part of the video is needed, else null")
    watch_until_s: int | None = Field(description="end second if only part of the video is needed, else null")
    confidence: float = Field(description="0-1: how sure you are this is the right video for this slot")
    confidence_note: str = Field(description="what would make you more or less sure")


class DroppedOut(BaseModel):
    video_id: str
    reason: str


class NearDupOut(BaseModel):
    kept: str
    dropped: str
    shared_topics: list[str]
    why_kept: str


class SelectOut(BaseModel):
    picks: list[PickOut] = Field(description="in the order the learner should watch them")
    dropped: list[DroppedOut] = Field(description="the strongest candidates that were NOT picked, and why")
    near_duplicates: list[NearDupOut]
    warnings: list[str] = Field(description="anything the learner should know: gaps, infeasibility, assumptions")


# ---------------------------------------------------------------- output


class Evidence(BaseModel):
    quote_id: str
    t: str  # mm:ss
    quote: str
    source: Literal["transcript", "chapters/description"] = "transcript"


class Pick(BaseModel):
    rank: int
    video_id: str
    title: str
    channel: str
    url: str
    duration_min: float
    minutes_counted: float
    watch_from: str | None = None
    watch_until: str | None = None
    covers: list[str]
    reason: str
    evidence: list[Evidence]
    confidence: float
    confidence_note: str
    level: str | None = None
    format: str | None = None


class Dropped(BaseModel):
    video_id: str
    title: str
    stage: Literal["prefilter", "language", "assess", "select"]
    reason: str


class Curriculum(BaseModel):
    persona_id: str
    goal: str
    budget_minutes: int
    total_minutes: float
    interpretation: str
    assumptions: list[str]
    feasible: bool
    feasibility_note: str
    sub_topics: list[SubTopic]
    picks: list[Pick]
    dropped: list[Dropped]
    near_duplicates: list[NearDupOut]
    warnings: list[str]
    pool_size: int
    models: dict[str, str]
    cost_usd: float
    latency_s: float
    mode: str = "agent"
