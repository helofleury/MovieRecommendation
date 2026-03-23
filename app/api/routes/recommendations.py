from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.models import User, Movie, Rating
from collections import defaultdict

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/recommendations/{user_id}")
def recommend_movies(user_id: int, db: Session = Depends(get_db)):
    ratings = db.query(Rating).all()

    # user -> {movie: score}
    user_ratings = defaultdict(dict)

    for r in ratings:
        user_ratings[r.user_id][r.movie_id] = r.score

    if user_id not in user_ratings:
        return {"message": "User has no ratings yet"}

    target_user = user_ratings[user_id]

    # calcular similaridade simples (número de filmes em comum)
    similarity = {}

    for other_user, other_ratings in user_ratings.items():
        if other_user == user_id:
            continue

        common_movies = set(target_user.keys()) & set(other_ratings.keys())
        similarity[other_user] = len(common_movies)

    # pegar usuários mais parecidos
    similar_users = sorted(similarity, key=similarity.get, reverse=True)

    # recomendações
    recommended_movies = {}

    for sim_user in similar_users:
        for movie_id, score in user_ratings[sim_user].items():
            if movie_id not in target_user:
                recommended_movies[movie_id] = score

    # ordenar por score
    recommended_movies = sorted(
        recommended_movies.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # buscar títulos
    result = []
    for movie_id, score in recommended_movies:
        movie = db.query(Movie).filter(Movie.id == movie_id).first()
        if movie:
            result.append({
                "movie": movie.title,
                "score": score
            })

    return result