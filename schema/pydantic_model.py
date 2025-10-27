from pydantic import BaseModel, Field



class Tweet(BaseModel):
    text: str = Field(
        ...,
        min_length=3,
        max_length=280,  
        description="Tweet text for sentiment analysis",
        example="I love this new phone!"
    )