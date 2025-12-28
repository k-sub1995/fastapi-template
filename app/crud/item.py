from typing import List, Optional

from app.models.item import Item
from app.schemas.item import ItemCreate

# Mock DB
MOCK_DB: List[Item] = []


def get_items() -> List[Item]:
    return MOCK_DB


def get_item(item_id: int) -> Optional[Item]:
    for item in MOCK_DB:
        if item.id == item_id:
            return item
    return None


def create_item(item_in: ItemCreate) -> Item:
    new_id = MOCK_DB[-1].id + 1 if MOCK_DB else 1

    db_obj = Item(id=new_id, title=item_in.title, description=item_in.description)
    MOCK_DB.append(db_obj)

    return db_obj
