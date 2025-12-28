from app.crud import item as crud
from app.schemas.item import Item, ItemCreate


def create_item_service(item_in: ItemCreate) -> Item:
    """
    Business logic for creating an item.

    Args:
        item_in (ItemCreate): Item schema to create.

    Returns:
        Item: Created item.
    """
    return crud.create_item(item_in)
