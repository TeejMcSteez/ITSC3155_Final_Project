# imports the necessary good stuff
from sqlalchemy.orm import Session
from api.models.reviews import Review
from api.schemas.reviews import ReviewCreate

# defines the CRUD operations for reviews
def create_review(db: Session, review: ReviewCreate):
    db_review = Review(
        customer_identifier=review.customer_identifier,
        star_rating=review.star_rating,
        review_details=review.review_details
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_reviews(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Review).offset(skip).limit(limit).all()

def get_review(db: Session, review_id: int):
    return db.query(Review).filter(Review.id == review_id).first()