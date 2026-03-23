from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.routes import recommendations
from app.api.routes import movies, ratings, users

# cria tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Movie Recommendation API")

app.include_router(users.router)
app.include_router(movies.router)
app.include_router(ratings.router)
app.include_router(recommendations.router)

@app.get("/")
def root():
    return {"message": "API rodando 🚀"}