import pytest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.database.base import Base
from app.database.connection import get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={
        "check_same_thread": False
    }
)


TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


@pytest.fixture
def db():

    Base.metadata.drop_all(bind=engine)

    Base.metadata.create_all(bind=engine)

    database = TestingSessionLocal()

    try:
        yield database
    finally:
        database.close()



@pytest.fixture
def client(db):

    def override_get_db():

        try:
            yield db

        finally:
            pass


    app.dependency_overrides[get_db] = override_get_db


    return TestClient(app)