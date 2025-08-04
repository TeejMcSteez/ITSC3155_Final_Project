#this goes on the api side

# imports the necessary good stuff
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# defines the basic structure of a review
class ReviewBase(BaseModel):
    star_rating: int = Field(..., ge=1, le=5)
    review_details: Optional[str] = None

# attaches the customer identifier to the review creation schema
class ReviewCreate(ReviewBase):
    customer_identifier: str

# defines the structure for reading the review
class ReviewRead(ReviewBase):
    id: int
    customer_identifier: str
    date: datetime

    class Config:
        orm_mode = True