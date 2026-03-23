from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str

class MovieCreate(BaseModel):
    title: str
    genre: str

class RatingCreate(BaseModel):
    user_id: int
    movie_id: int
    score: float