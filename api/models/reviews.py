#this goes in the database side

# imports the necessary good stuff
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from api.dependencies.database import Base

# defines the basic structure of a review
class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    customer_identifier = Column(String, nullable=False)
    star_rating = Column(Integer, nullable=False)
    review_details = Column(String, nullable=True)
    date = Column(DateTime(timezone=True), server_default=func.now())