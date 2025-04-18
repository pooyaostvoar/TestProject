import pytest
from app.database import engine
from sqlmodel import  SQLModel


@pytest.fixture(scope="function", autouse=True)
def setup_db():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)
    yield
    SQLModel.metadata.drop_all(engine)
