# 🎬 Movie Recommendation API

A scalable and modular backend application that allows users to rate movies and receive personalized recommendations based on collaborative filtering.

---

## 🚀 Overview

This project is a RESTful API designed to simulate a real-world recommendation system similar to platforms like Netflix or Amazon.

It enables users to:

- Create accounts  
- Add and browse movies  
- Rate movies  
- Receive personalized recommendations  

The system is built following clean architecture principles, focusing on scalability, maintainability, and clarity.

---

## 🧠 Features

- User management  
- Movie catalog  
- Movie rating system  
- Recommendation engine (user-based collaborative filtering)  
- Modular architecture  
- Automatic API documentation with Swagger  

---

## 🏗️ Architecture
```
app/
├── api/ # Routes (controllers)
├── models/ # Database models
├── schemas/ # Data validation
├── db/ # Database configuration
└── main.py # Application entry point
```
---

## ⚙️ Tech Stack

- Python  
- FastAPI  
- SQLAlchemy  
- SQLite (development)  

---

## ▶️ Running the Project

### 1. Clone the repository
```bash
git clone https://github.com/helofleury/MovieRecommendation.git
cd MovieRecommendation

## 2. Install dependencies
```bash
pip install fastapi uvicorn sqlalchemy
```

## 3. Run the server
```bash
uvicorn app.main:app --reload
```

---

## 📚 API Documentation

After running the server, access:

```
http://127.0.0.1:8000/docs
```

Use **Swagger UI** to test all endpoints interactively.

---

## 🔌 API Endpoints

### Users
- `POST /users` → Create user

### Movies
- `POST /movies` → Add movie  
- `GET /movies` → List movies

### Ratings
- `POST /ratings` → Rate a movie

### Recommendations
- `GET /recommendations/{user_id}` → Get personalized recommendations

---

## 🤖 Recommendation System

The recommendation engine is based on **user-based collaborative filtering**:

- Identify users with similar preferences  
- Compare shared movie ratings  
- Recommend unseen movies liked by similar users  

---

## 🧪 Example Workflow

1. Create users  
2. Add movies  
3. Users rate movies  
4. Request recommendations  

---

## 💡 Key Learnings

- Backend API design  
- Database modeling  
- Clean architecture  
- Recommendation systems  
- Real-world development practices  
