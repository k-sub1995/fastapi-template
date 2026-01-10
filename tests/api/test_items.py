"""Tests for the items API endpoints."""

from fastapi.testclient import TestClient

from app.crud import item as crud
from app.main import app

client = TestClient(app)


def setup_function():
    """Clear mock DB before each test."""
    crud.MOCK_DB.clear()


class TestRootEndpoint:
    """Tests for the root endpoint."""

    def test_read_root(self):
        """Test that root endpoint returns welcome message."""
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to FastAPI template API"}


class TestItemsEndpoints:
    """Tests for the items API endpoints."""

    def test_read_items_empty(self):
        """Test reading items when database is empty."""
        crud.MOCK_DB.clear()
        response = client.get("/api/v1/items/")
        assert response.status_code == 200
        assert response.json() == []

    def test_create_item(self):
        """Test creating a new item."""
        crud.MOCK_DB.clear()
        item_data = {"title": "Test Item", "description": "Test Description"}
        response = client.post("/api/v1/items/", json=item_data)
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Test Item"
        assert data["description"] == "Test Description"
        assert data["id"] == 1

    def test_create_item_without_description(self):
        """Test creating an item without description."""
        crud.MOCK_DB.clear()
        item_data = {"title": "Item Without Description"}
        response = client.post("/api/v1/items/", json=item_data)
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "Item Without Description"
        assert data["description"] is None

    def test_read_items_after_create(self):
        """Test reading items after creating one."""
        crud.MOCK_DB.clear()
        item_data = {"title": "Test Item", "description": "Test Description"}
        client.post("/api/v1/items/", json=item_data)

        response = client.get("/api/v1/items/")
        assert response.status_code == 200
        items = response.json()
        assert len(items) == 1
        assert items[0]["title"] == "Test Item"

    def test_read_item_by_id(self):
        """Test reading a specific item by ID."""
        crud.MOCK_DB.clear()
        item_data = {"title": "Test Item", "description": "Test Description"}
        create_response = client.post("/api/v1/items/", json=item_data)
        item_id = create_response.json()["id"]

        response = client.get(f"/api/v1/items/{item_id}")
        assert response.status_code == 200
        assert response.json()["id"] == item_id
        assert response.json()["title"] == "Test Item"

    def test_read_item_not_found(self):
        """Test reading a non-existent item returns 404."""
        crud.MOCK_DB.clear()
        response = client.get("/api/v1/items/999")
        assert response.status_code == 404
        assert response.json()["detail"] == "Item not found"

    def test_create_multiple_items(self):
        """Test creating multiple items generates sequential IDs."""
        crud.MOCK_DB.clear()
        for i in range(3):
            item_data = {"title": f"Item {i + 1}"}
            response = client.post("/api/v1/items/", json=item_data)
            assert response.json()["id"] == i + 1

        response = client.get("/api/v1/items/")
        assert len(response.json()) == 3
