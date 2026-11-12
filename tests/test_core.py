"""Offline unit tests: no network, no LLM."""

from curriculum.dedup import clusters, topic_overlap
from curriculum.llm import strict_schema
from curriculum.models import AssessOut, Assessment, Candidate, PickOut, PlanOut, Snippet
from curriculum.selection import counted_minutes
from curriculum.verify import locate_quote
from curriculum.youtube import make_windows, ts, window_lines
from evals.agreement import compare, kappa


WORDS = "alpha bravo charlie delta echo foxtrot golf hotel india juliet kilo lima mike november oscar papa quebec romeo sierra tango".split()


def snippets(n, step=5.0):
    # every line distinct, like real speech
    return [Snippet(start=i * step, text=f"{WORDS[i % 20]} {WORDS[(i // 20) % 20]} {WORDS[(i * 7) % 20]} step {i} we run npm create vite") for i in range(n)]


def test_short_video_is_passed_whole():
    w = make_windows(snippets(100), duration_s=500)
    lines = window_lines(w)
    assert lines[0][0] == 0 and lines[-1][0] >= 480
    assert "---" not in w  # no window separators for short videos


def test_long_video_is_windowed_and_capped():
    sn = snippets(4000, step=3.0)  # 200 minutes
    w = make_windows(sn, duration_s=12000)
    assert "---" in w
    assert len(w.split()) <= 5000
    starts = [t for t, _ in window_lines(w)]
    assert starts == sorted(starts) and starts[-1] > 6000  # reaches deep into the video


def test_ts_formats():
    assert ts(65) == "01:05" and ts(3725) == "1:02:05"


def test_quote_found_near_timestamp_and_rejected_when_invented():
    w = make_windows(snippets(60), duration_s=300)
    ok, at, _ = locate_quote(snippets(60)[12].text, w, t=60)
    assert ok and abs(at - 60) <= 20
    bad, _, _ = locate_quote("today we deploy a kubernetes cluster on aws", w, t=60)
    assert not bad


def test_quote_with_wrong_timestamp_still_found():
    w = make_windows(snippets(60), duration_s=300)
    ok, at, _ = locate_quote(snippets(60)[50].text, w, t=10)
    assert ok and at >= 240


def test_strict_schema_requires_everything_and_keeps_title_fields():
    s = strict_schema(PlanOut)
    sub = s["properties"]["sub_topics"]["items"]
    assert "title" in sub["properties"] and set(sub["required"]) == set(sub["properties"])
    assert s["additionalProperties"] is False
    assert "$defs" not in s and "$ref" not in str(s)
    assert "format" in strict_schema(AssessOut)["properties"]  # a field named like a JSON-schema keyword survives


def _a(vid, topics, level="beginner", fmt="project_build"):
    return Assessment(video_id=vid, spoken_language="en", summary="", topics_covered=topics, level=level, format=fmt,
                      is_project_based=True, project_built="", tools_and_versions=[], red_flags=[], quotes=[],
                      segments=[], relevance=[])


def test_topic_overlap_is_fuzzy():
    score, shared = topic_overlap(["usestate hook", "localstorage", "vite setup"], ["usestate", "localstorage", "props"])
    assert score >= 0.5 and "localstorage" in shared


def test_clusters_group_near_duplicates_only():
    a = {"x": _a("x", ["usestate", "localstorage", "todo app"]), "y": _a("y", ["usestate hook", "localstorage", "todo app"]),
         "z": _a("z", ["vite", "project structure"])}
    cs = clusters(a)
    assert len(cs) == 1 and set(cs[0]["members"]) == {"x", "y"}


def test_clusters_respect_level():
    a = {"x": _a("x", ["usestate", "localstorage"]), "y": _a("y", ["usestate", "localstorage"], level="advanced")}
    assert clusters(a) == []


def test_counted_minutes_uses_watch_range():
    c = Candidate(video_id="abcdefghijk", title="t", duration_s=3600)
    p = PickOut(video_id=c.video_id, covers=[], reason="", evidence_quote_ids=[], watch_from_s=600, watch_until_s=1500,
                confidence=0.5, confidence_note="")
    assert counted_minutes(p, c) == 15.0
    p.watch_from_s = p.watch_until_s = None
    assert counted_minutes(p, c) == 60.0


def test_kappa_and_rates():
    assert kappa([1, 0, 1, 0], [1, 0, 1, 0]) == 1.0
    r = compare([1, 1, 0, 0, 1, 0], [1, 0, 0, 1, 1, 0])
    assert r["tpr"] == round(2 / 3, 2) and r["tnr"] == round(2 / 3, 2)


def test_unavailable_detection():
    from curriculum.youtube import is_unavailable

    assert is_unavailable({"error": "DownloadError: ERROR: [youtube] abc: This video is not available"})
    assert is_unavailable({"error": "DownloadError: ERROR: [youtube] abc: Private video. Sign in if you've been granted access"})
    assert not is_unavailable({"error": "TimeoutError: timed out"})
    assert not is_unavailable({"description": "fine"})


def test_metadata_fallback_never_labels_empty_evidence():
    from curriculum.discover import metadata_fallback

    w, kind = metadata_fallback({"description": "We build a CLI", "chapters": [{"start": 60, "title": "Borrowing"}]}, "")
    assert kind == "metadata" and "[01:00] (chapter) Borrowing" in w
    w, kind = metadata_fallback({"error": "DownloadError: Sign in to confirm you're not a bot"}, "short search snippet")
    assert kind == "metadata" and "short search snippet" in w
    assert metadata_fallback({"error": "x"}, "") == ("", "none")


def test_course_slices_allowed_only_without_overlap():
    from curriculum.models import SelectOut
    from curriculum.selection import _sanitize

    c = Candidate(video_id="abcdefghijk", title="course", duration_s=36000)
    a = _a(c.video_id, ["pytorch"])

    def pk(f, u):
        return PickOut(video_id=c.video_id, covers=[], reason="", evidence_quote_ids=[], watch_from_s=f, watch_until_s=u,
                       confidence=0.5, confidence_note="")

    out = SelectOut(picks=[pk(0, 3600), pk(7200, 9000), pk(8000, 9500), pk(None, None)], dropped=[], near_duplicates=[], warnings=[])
    fixes = []
    out = _sanitize(out, {c.video_id: c}, {c.video_id: a}, fixes)
    assert [(p.watch_from_s, p.watch_until_s) for p in out.picks] == [(0, 3600), (7200, 9000)]
    assert len(fixes) == 2


def test_data_api_helpers():
    from curriculum import youtube

    assert youtube._iso_duration("PT1H2M3S") == 3723
    assert youtube._iso_duration("PT45S") == 45
    assert youtube._iso_duration("P1DT1M") == 86460
    assert youtube._iso_duration("") == 0
    desc = "Intro text\n0:00 Intro\n2:15 - Setup with Vite\n(12:40) useState\n1:02:03 Deploy"
    assert youtube.parse_chapters(desc) == [
        {"start": 0, "title": "Intro"}, {"start": 135, "title": "Setup with Vite"},
        {"start": 760, "title": "useState"}, {"start": 3723, "title": "Deploy"}]
    assert youtube.parse_chapters("1:00 a\n2:00 b\n3:00 c") == []  # must start at 0:00
    assert youtube.parse_chapters("0:00 a\n2:00 b") == []  # fewer than 3
    d = youtube._details_from_item({"snippet": {"title": "T", "channelTitle": "C", "description": "x", "publishedAt": "2025-03-04T10:00:00Z",
                                                "defaultAudioLanguage": "en"},
                                    "contentDetails": {"duration": "PT10M", "caption": "false"}, "statistics": {"viewCount": "12"}})
    assert (d["duration_s"], d["upload_date"], d["view_count"], d["has_uploaded_captions"], d["language"]) == (600, "20250304", 12, False, "en")


def test_flagged_pick_needs_no_unflagged_alternative():
    from curriculum.models import Assessment, Candidate, PickOut, SelectOut
    from curriculum.selection import flag_conflicts

    def asm(flags, score):
        return Assessment.model_construct(red_flags=flags, relevance=[type("R", (), {"sub_topic_id": "s1", "score": score})()])

    pool = {v: Candidate(video_id=v, title=v, duration_s=600) for v in ("aaaaaaaaaaa", "bbbbbbbbbbb", "ccccccccccc")}
    pick = PickOut(video_id="aaaaaaaaaaa", covers=["s1"], reason="", evidence_quote_ids=[], watch_from_s=None, watch_until_s=None,
                   confidence=0.5, confidence_note="")
    out = SelectOut.model_construct(picks=[pick], dropped=[], warnings=[])
    # off_topic is a context-independent blocking flag the code enforces; bbbbbbbbbbb (unflagged, teaches s1) is the alternative.
    assessments = {"aaaaaaaaaaa": asm(["off_topic"], 3), "bbbbbbbbbbb": asm([], 2), "ccccccccccc": asm(["off_topic"], 3)}
    [(p, flags, alts)] = flag_conflicts(out, pool, assessments)
    assert flags == ["off_topic"] and alts == ["bbbbbbbbbbb"]
    assessments["bbbbbbbbbbb"] = asm([], 1)  # mentions s1 only (score 1): not real coverage, so not an alternative
    assert flag_conflicts(out, pool, assessments)[0][2] == []
    assessments["aaaaaaaaaaa"] = asm(["pure_theory"], 3)  # learner-relative: left to the prompt, not blocked in code
    assert flag_conflicts(out, pool, assessments) == []


def test_learner_limits():
    from curriculum.models import Candidate, Expectations, Pick
    from evals.checks import learner_limits

    def pick(vid, ch, mins):
        return Pick.model_construct(video_id=vid, channel=ch, minutes_counted=mins)

    pool = {"a": Candidate(video_id="a", title="", upload_date="20210105"), "b": Candidate(video_id="b", title="", upload_date="20240301"),
            "c": Candidate(video_id="c", title="", upload_date=None)}
    picks = [pick("a", "X", 40), pick("b", "X", 95), pick("c", "Y", 10)]
    m = learner_limits(picks, pool, Expectations(min_upload_year=2022, max_sitting_minutes=90, max_per_channel=1, max_channels=1))
    assert m["too_old_list"] == ["a"] and not m["recency_ok"]  # unknown dates are not counted as old
    assert m["too_long_list"] == ["b (95 min)"] and not m["sitting_ok"]
    assert not m["creators_ok"] and len(m["creator_issue_list"]) == 2
    assert all(learner_limits(picks, pool, Expectations())[k] for k in ("recency_ok", "sitting_ok", "creators_ok"))


def test_agent_loop_tools_and_validation():
    from curriculum.agent_loop import _counted, _read, _search, _validate
    from curriculum.models import Assessment, Candidate, Quote

    pool = {
        "aaaaaaaaaaa": Candidate(video_id="aaaaaaaaaaa", title="React hooks tutorial", channel="X", duration_s=600, view_count=100, found_by=["react hooks"]),
        "bbbbbbbbbbb": Candidate(video_id="bbbbbbbbbbb", title="Vue basics", channel="Y", duration_s=1200, view_count=50, found_by=["vue"]),
    }
    # search ranks by token overlap with the query
    res = _search(pool, "react hooks", k=5)
    assert res["results"][0]["video_id"] == "aaaaaaaaaaa"
    # counted minutes is robust to a string / missing watch range
    assert _counted({}, pool["aaaaaaaaaaa"]) == 10.0
    assert _counted({"watch_from_s": "60", "watch_until_s": "360"}, pool["aaaaaaaaaaa"]) == 5.0  # strings coerced
    assert _counted({"watch_from_s": "oops"}, pool["aaaaaaaaaaa"]) == 10.0  # bad value ignored

    a = Assessment.model_construct(summary="teaches hooks", level="intermediate", format="tutorial", red_flags=[],
                                   topics_covered=["hooks"], project_built="", evidence_source="transcript",
                                   quotes=[Quote(id="q1", t=12, text="use state"), Quote(id="q2", t=20, text="unverified")],
                                   verified_quote_ids=["q1"])
    read = _read({"aaaaaaaaaaa": a}, pool, "aaaaaaaaaaa")
    assert read["success"] and [q["id"] for q in read["quotes"]] == ["q1"]  # only verified quotes exposed
    assert _read({}, pool, "zzz")["success"] is False

    # validation: unread pick, unknown id, over budget, empty
    errs = _validate({"picks": [{"video_id": "aaaaaaaaaaa"}]}, pool, {}, set(), budget=30)
    assert any("read_video" in e for e in errs)  # not read yet
    assert _validate({"picks": []}, pool, {}, set(), 30) == ["no picks: a curriculum needs at least one video"]
    assert _validate({"picks": [{"video_id": "zzz"}]}, pool, {}, {"zzz"}, 30)[0].endswith("not a real video id")
    over = _validate({"picks": [{"video_id": "bbbbbbbbbbb"}]}, pool, {}, {"bbbbbbbbbbb"}, budget=5)  # 20 min > 5
    assert any("budget" in e for e in over)


def test_strict_schema_strips_keywords_but_not_fields_named_like_them():
    from pydantic import BaseModel, Field

    class Odd(BaseModel):
        default: str
        pattern: dict = Field(default={"a": 1})
        count: int = Field(default=3, ge=0, le=9)

    s = strict_schema(Odd)
    assert set(s["properties"]) == {"default", "pattern", "count"}  # fields NAMED like keywords survive
    assert "default" not in s["properties"]["count"] and "minimum" not in s["properties"]["count"]
    assert "default" not in s["properties"]["pattern"]  # a dict-valued default does not leak into the schema
    assert set(s["required"]) == {"default", "pattern", "count"}


def test_sanitize_drops_pick_without_assessment():
    from curriculum.models import SelectOut
    from curriculum.selection import _sanitize

    pool = {"aaaaaaaaaaa": Candidate(video_id="aaaaaaaaaaa", title="t", duration_s=600)}
    pick = PickOut(video_id="aaaaaaaaaaa", covers=[], reason="", evidence_quote_ids=[], watch_from_s=None,
                   watch_until_s=None, confidence=0.5, confidence_note="")
    fixes: list[str] = []
    out = _sanitize(SelectOut.model_construct(picks=[pick], dropped=[], warnings=[]), pool, {}, fixes)
    assert out.picks == [] and any("no assessment" in f for f in fixes)


def test_flag_conflicts_skips_pick_without_assessment():
    from curriculum.models import SelectOut
    from curriculum.selection import flag_conflicts

    pool = {"aaaaaaaaaaa": Candidate(video_id="aaaaaaaaaaa", title="", duration_s=600)}
    pick = PickOut(video_id="aaaaaaaaaaa", covers=["s1"], reason="", evidence_quote_ids=[], watch_from_s=None,
                   watch_until_s=None, confidence=0.5, confidence_note="")
    assert flag_conflicts(SelectOut.model_construct(picks=[pick], dropped=[], warnings=[]), pool, {}) == []


def test_qa_referenced_ids_ignore_bare_words():
    from curriculum.qa import _referenced_ids

    known, pool = {"aaaaaaaaaaa"}, {"aaaaaaaaaaa", "bbbbbbbbbbb"}
    assert _referenced_ids("why not https://youtu.be/ccccccccccc here", known, pool) == ["ccccccccccc"]
    assert _referenced_ids("Recommended videos seem thin", known, pool) == []  # 11-letter first word
    assert _referenced_ids("approx_2024 budget still fine?", known, pool) == []  # id-shaped word with digits
    assert _referenced_ids("bbbbbbbbbbb — why was this dropped?", known, pool) == ["bbbbbbbbbbb"]  # real pool id
    assert _referenced_ids("v=aaaaaaaaaaa again", known, pool) == []  # already assessed -> nothing to fetch


def test_agent_loop_tools_expose_upload_dates():
    from curriculum.agent_loop import _read, _search
    from curriculum.models import Quote

    pool = {"aaaaaaaaaaa": Candidate(video_id="aaaaaaaaaaa", title="React hooks", channel="X", duration_s=600,
                                     view_count=10, upload_date="20240105", found_by=["react"])}
    assert _search(pool, "react", k=3)["results"][0]["uploaded"] == "20240105"
    a = Assessment.model_construct(summary="", level="beginner", format="tutorial", red_flags=[], topics_covered=[],
                                   project_built="", evidence_source="transcript", quotes=[], verified_quote_ids=[])
    assert _read({"aaaaaaaaaaa": a}, pool, "aaaaaaaaaaa")["uploaded"] == "20240105"


def test_continue_loop_validates_revision(tmp_path, monkeypatch):
    import json as _json
    from types import SimpleNamespace as NS

    import curriculum.agent_loop as al

    plan = {"interpretation": "", "assumptions": [], "feasible": True, "feasibility_note": "",
            "preferred_language": "en", "learner_level": "beginner", "sub_topics": [], "search_queries": [],
            "title_exclusions": [], "skip_topics": []}
    conv = {"persona": {"persona_id": "p", "goal": "g", "time_budget_minutes": 30,
                        "user_context": {"background": "", "known": [], "unknown": [], "constraints": ""}},
            "pool": [{"video_id": "aaaaaaaaaaa", "title": "t", "duration_s": 600}],
            "assessments": {}, "base_plan": plan, "read_ids": [], "messages": []}
    (tmp_path / "conversation.json").write_text(_json.dumps(conv))

    # turn 1: the model tries to submit a revision with an unread pick; turn 2: it answers in text.
    scripted = [NS(content="", tool_calls=[NS(id="1", function=NS(name="submit_curriculum",
                                              arguments=_json.dumps({"picks": [{"video_id": "aaaaaaaaaaa"}]})))]),
                NS(content="That pick failed validation, so I left the curriculum unchanged.", tool_calls=None)]
    monkeypatch.setattr(al, "chat_tools", lambda *a, **k: scripted.pop(0))

    events: list[dict] = []
    answer, changed, cur = al.continue_loop(tmp_path, "please swap the video", on_event=events.append)
    assert changed is False and cur is None and "unchanged" in answer
    assert any(e["kind"] == "retry" for e in events)  # the invalid revision was rejected, not silently accepted
    saved = _json.loads((tmp_path / "conversation.json").read_text())
    assert len(saved["messages"]) > 0  # the extended conversation was persisted for the next follow-up


def test_transcription_backoff_order(monkeypatch):
    import curriculum.youtube as yt

    monkeypatch.setattr(yt.gemini_budget, "cap", 1.0)
    monkeypatch.setattr(yt, "_transcribe_openrouter", lambda v, l: {"error": "Gemini no content (length)"})
    ok = {"snippets": [{"start": 0.0, "text": "hi"}], "lang": "en", "generated": True, "error": None, "source": "gemini"}
    monkeypatch.setattr(yt, "_transcribe_google_direct", lambda v, l: ok)

    monkeypatch.delenv("GEMINI_API_KEY", raising=False)  # no key -> no direct-API call, the error stands
    assert yt._gemini_transcript("aaaaaaaaaaa", ["en"])["error"] == "Gemini no content (length)"
    monkeypatch.setenv("GEMINI_API_KEY", "test")  # key set -> the last backoff rescues the transcript
    assert yt._gemini_transcript("aaaaaaaaaaa", ["en"]) == ok
    monkeypatch.setattr(yt, "_transcribe_openrouter", lambda v, l: ok)  # OpenRouter first when it works
    monkeypatch.setattr(yt, "_transcribe_google_direct", lambda v, l: (_ for _ in ()).throw(AssertionError("must not be called")))
    assert yt._gemini_transcript("aaaaaaaaaaa", ["en"]) == ok
