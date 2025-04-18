from fastapi import FastAPI
from app.database import engine
from app.apis import router as api_router
from sqlmodel import SQLModel

app = FastAPI()

SQLModel.metadata.create_all(engine)

app.include_router(api_router)
