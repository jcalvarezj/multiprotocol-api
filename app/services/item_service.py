from ..models.item import Item
from ..repositories.item_repository import ItemRepository


class ItemService:
    def __init__(self):
        self.repository = ItemRepository()

    def get_all_items(self):
        return self.repository.get_all()

    def get_item_by_id(self, item_id):
        return self.repository.get_item_by_id(item_id)

    def create_item(self, item: Item):
        return self.repository.create(item)
