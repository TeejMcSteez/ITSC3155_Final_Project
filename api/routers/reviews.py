from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.dependencies.database import get_db
from api.controllers.reviews import create_review, get_reviews, get_review
from api.schemas.reviews import ReviewCreate, ReviewRead

router = APIRouter(prefix="/reviews", tags=["reviews"])

@router.post("/", response_model=ReviewRead)
def create_customer_review(
    review: ReviewCreate,
    db: Session = Depends(get_db)
):
    return create_review(db, review)

@router.get("/", response_model=list[ReviewRead])
def list_reviews(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_reviews(db, skip=skip, limit=limit)

@router.get("/{review_id}", response_model=ReviewRead)
def read_review(review_id: int, db: Session = Depends(get_db)):
    review = get_review(db, review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

