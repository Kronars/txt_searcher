import pytest
from fastapi.testclient import TestClient
from sqlalchemy_utils import database_exists

from app.main import app
from app.crud import es
from app.db import Session


@pytest.fixture()
def test_app():
    client = TestClient(app)
    yield client
