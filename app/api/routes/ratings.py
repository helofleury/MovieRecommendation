from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.models import Rating
from app.schemas.schemas import RatingCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/ratings")
def rate_movie(rating: RatingCreate, db: Session = Depends(get_db)):
    new_rating = Rating(
        user_id=rating.user_id,
        movie_id=rating.movie_id,
        score=rating.score
    )
    db.add(new_rating)
    db.commit()
    db.refresh(new_rating)
    return new_rating