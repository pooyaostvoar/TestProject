from fastapi import FastAPI
from app.database import engine

from sqlmodel import SQLModel

app = FastAPI()

SQLModel.metadata.create_all(engine)

@app.get("/")
def hello():
    return 'hello'


