"""The LangGraph state schema threaded through every node."""

from typing import TypedDict
from job_search import Profile, JobPostings, RankedJob, TailoringPack

class AgentState(TypedDict, total=False):
    """Mutable state passed between nodes.
    ``total=False`` lets nodes return partial updates and lets the initial invoke
    payload set only the fields it has. ``llm_calls``, ``errors`` and
    ``jobs_sources`` back the call budget, non-crashing error handling and trace
    metadata respectively.
    """

    cv_text: str
    profile: Profile | None
    search_query: str | None
    jobs: list[JobPostings]
    ranked_jobs: list[RankedJob]
    reformulation_count: int
    llm_calls: int
    errors: list[str]
    jobs_sources: list[str]
    tailoring: TailoringPack | None
    selected_job_id: str | None
