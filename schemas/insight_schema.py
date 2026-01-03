from pydantic import BaseModel, Field
from typing import List, Literal


class CallInsights(BaseModel):
    """
    Structured intelligence extracted from a sales call transcript.
    """

    top_topics: List[str] = Field(
        description="Key medical, clinical, or product topics discussed in the call"
    )

    objections: List[str] = Field(
        description="Concerns or objections raised by the healthcare professional"
    )

    competitors_mentioned: List[str] = Field(
        description="Competitor brands or products mentioned during the call"
    )

    product_sentiment: Literal["positive", "neutral", "negative"] = Field(
        description="Overall sentiment of the HCP towards the product"
    )

    next_best_action: str = Field(
        description="One clear, actionable next step for the sales representative"
    )
