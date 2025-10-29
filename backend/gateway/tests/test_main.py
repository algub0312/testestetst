from typing import Generator

import pytest
from fastapi.testclient import TestClient

from main import app

STATUS_CODE_OK = 200


@pytest.fixture
def client() -> Generator[TestClient]:
    """Fixture to initialize the FastAPI TestClient, using the mocked messaging manager."""  # noqa: E501
    with TestClient(app) as client:
        yield client


def test_root(client: TestClient) -> None:
    """Test the root endpoint (GET /)."""
    response = client.get("/")
    assert response.status_code == STATUS_CODE_OK
    assert response.json() == {"message": "Welcome to the API Gateway"}


def test_health(client: TestClient) -> None:
    """Test the health check endpoint (GET /health)."""
    response = client.get("/health")
    assert response.status_code == STATUS_CODE_OK
    assert response.json() == {"status": "ok"}
