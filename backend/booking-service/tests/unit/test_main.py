from typing import Generator
from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi.testclient import TestClient

from main import app
from src.messaging.messaging_manager import messaging_manager

STATUS_CODE_OK = 200


# Mocking messaging manager to prevent real connection attempts during testing
@pytest.fixture
def mock_messaging_manager() -> MagicMock:
    """Mock the messaging manager for testing purposes."""
    mock = MagicMock()
    mock.start_all = AsyncMock()
    mock.stop_all = AsyncMock()
    mock.add_pubsub = MagicMock()

    # Assign the mocked methods to the actual messaging manager
    messaging_manager.add_pubsub = mock.add_pubsub
    messaging_manager.start_all = mock.start_all
    messaging_manager.stop_all = mock.stop_all
    return mock


@pytest.fixture
def client(mock_messaging_manager: MagicMock) -> Generator[TestClient]:
    """Fixture to initialize the FastAPI TestClient, using the mocked messaging manager."""  # noqa: E501
    with TestClient(app) as client:
        yield client


def test_root(client: TestClient) -> None:
    """Test the root endpoint (GET /)."""
    response = client.get("/")
    assert response.status_code == STATUS_CODE_OK
    assert response.json() == {"service": "Desk Booking Service"}


def test_health(client: TestClient) -> None:
    """Test the health check endpoint (GET /health)."""
    response = client.get("/health")
    assert response.status_code == STATUS_CODE_OK
    assert response.json() == {"status": "ok"}


def test_dummy1() -> None:
    """A dummy test to ensure the test suite runs."""
    assert True


def test_dummy2() -> None:
    """A dummy test to ensure the test suite runs."""
    assert True
