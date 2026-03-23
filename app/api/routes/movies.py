from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.models import Movie
from app.schemas.schemas import MovieCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/movies")
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    new_movie = Movie(title=movie.title, genre=movie.genre)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie

@router.get("/movies")
def list_movies(db: Session = Depends(get_db)):
    return db.query(Movie).all()