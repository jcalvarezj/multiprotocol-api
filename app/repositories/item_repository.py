from typing import List
from ..models.item import Item


class ItemRepository:
    def __init__(self):
        self.fake_db: List[Item] = []

    def get_all(self) -> List[Item]:
        return self.fake_db

    def get_item_by_id(self, item_id) -> List[Item]:
        items = list(filter(lambda x: x.id == item_id, self.fake_db))
        return items[0] if len(items) else None

    def create(self, item: Item) -> Item:
        self.fake_db.append(item)
        return item
