"""Pytest configuration and fixtures.

This module contains shared fixtures for testing the FastAPI application.
"""

from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="module")
def client() -> Generator[TestClient, None, None]:
    """Create a test client for the FastAPI application.

    Yields:
        TestClient: A test client instance for making HTTP requests.
    """
    with TestClient(app) as c:
        yield c
