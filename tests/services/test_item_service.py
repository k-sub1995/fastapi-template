"""Tests for the item service layer."""

from app.crud import item as crud
from app.schemas.item import ItemCreate
from app.services import item_service


def setup_function():
    """Clear mock DB before each test."""
    crud.MOCK_DB.clear()


class TestItemService:
    """Tests for item_service functions."""

    def test_create_item_service(self):
        """Test creating an item through the service layer."""
        crud.MOCK_DB.clear()
        item_in = ItemCreate(title="Service Test", description="Created via service")
        result = item_service.create_item_service(item_in)

        assert result.id == 2
        assert result.title == "Service Test"
        assert result.description == "Created via service"

    def test_create_item_service_without_description(self):
        """Test creating an item without description through service."""
        crud.MOCK_DB.clear()
        item_in = ItemCreate(title="No Description Item")
        result = item_service.create_item_service(item_in)

        assert result.id == 1
        assert result.title == "No Description Item"
        assert result.description is None

    def test_create_item_service_persists_to_db(self):
        """Test that created items are persisted in mock DB."""
        crud.MOCK_DB.clear()
        item_in = ItemCreate(title="Persisted Item", description="Should be in DB")
        item_service.create_item_service(item_in)

        # Verify item is in the mock DB
        assert len(crud.MOCK_DB) == 1
        assert crud.MOCK_DB[0].title == "Persisted Item"
