from typing import List

from fastapi import APIRouter, HTTPException

from app.crud import item as crud
from app.schemas.item import Item, ItemCreate
from app.services import item_service

router = APIRouter()


@router.get("/", response_model=List[Item])
def read_items():
    """
    Get all items.

    Returns:
        List[Item]: All items.
    """
    items = crud.get_items()
    return items


@router.post("/", response_model=Item)
def create_item(item_in: ItemCreate):
    """
    Create new item.

    Args:
        item_in (ItemCreate): Item schema to create.

    Returns:
        Item: Created item.
    """
    return item_service.create_item_service(item_in)


@router.get("/{item_id}", response_model=Item)
def read_item(item_id: int):
    """
    Retrieve a specific item by ID.

    Args:
        item_id (int): The ID of the item to retrieve.

    Raises:
        HTTPException: Item not found.

    Returns:
        Item: Requested item.
    """
    db_item = crud.get_item(item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
