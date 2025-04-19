
# 🐳 Docker Setup for Local Development

This project uses Docker and Docker Compose to simplify local development and manage dependencies like the PostgreSQL database.

---

## 📁 Environment Setup

Before running the application, create a `.env` file in the root of your project with the following variables:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=bookdb
DATABASE_URL=postgresql+psycopg2://postgres:password@db:5432/bookdb
```

These are used by both the `db` and `web` services in Docker Compose.

---

## ⚙️ Services Overview

### 📦 `db` (PostgreSQL)

- Based on the `postgres:15` image  
- Stores data in a persistent Docker volume  
- Listens on port `5433` (maps to internal `5432`)

### 🚀 `web` (FastAPI App)

- Runs the FastAPI app with `uvicorn`  
- Reloads code automatically on changes  
- Depends on `db`  
- Uses the `DATABASE_URL` from `.env`

---

## ▶️ Running the App

To build and run the containers:

```bash
docker-compose up --build
```

To stop the containers:

```bash
docker-compose down
```

---

## 📘 API Docs

Once the app is running, explore the API documentation:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

These tools show available endpoints, schemas, and example `curl` commands.