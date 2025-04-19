
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
You can also check this [README](https://github.com/pooyaostvoar/TestProject/blob/main/app/apis/README.md)


---
## Testing

### Overview
The project uses SQLite for testing purposes to ensure lightweight and fast testing. When running the tests, the SQLite database is used by default, and it is set up and torn down automatically before and after each test.

### Running Tests Locally
To run the tests locally, ensure you have all dependencies installed and set up the environment as follows:

1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the tests with pytest. You can use the following command:

    ```bash
    PYTHONPATH=. pytest
    ```

   This command will run all tests and ensure that Python can correctly find your modules, especially when they are in subdirectories or not in the same directory as your test file. The `PYTHONPATH` is set to the current directory (`.`) to ensure that your code is correctly imported during testing.

### Test Environment
- **Database**: The tests are run using SQLite by default. 
- **Test Setup**: Each test is run in isolation with a fresh database setup, ensuring that tests are independent and there is no data persistence between tests.

### Continuous Integration
On every pull request, the tests will run in a GitHub Actions CI pipeline using the same SQLite setup, ensuring that all tests pass before merging the PR.

For more details about the CI pipeline, see the `ci.yml` file in the `.github/workflows` directory.


---

## 🛠️ Database Migrations

### Local Development (SQLite)

For local development, the database is configured to use SQLite (when you're running the tests).

### Switching to PostgreSQL in Production

To switch to PostgreSQL in production:

1. Modify the `DATABASE_URL` in your `.env` file to use PostgreSQL (e.g., `postgresql+psycopg2://user:password@host:port/database`).

2. Update the `sqlalchemy.url` setting in the `alembic.ini` file to point to the production PostgreSQL database:

   ```ini
   sqlalchemy.url = postgresql+psycopg2://user:password@host:5432/production_db
   ```
For more detail you can check this [README](https://github.com/pooyaostvoar/TestProject/blob/main/alembic/README)

