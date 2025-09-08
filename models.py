from pydantic import BaseModel
from typing import List

class CollectRequest(BaseModel):
    profile: dict
    posts: List[dict]

class SummaryResponse(BaseModel):
    summary: str

class RecommendResponse(BaseModel):
    caption: str
    hashtags: List[str]
    justification: str
