from fastapi import APIRouter, HTTPException
from ..models.item import Item
from ..schemas.item_schema import ItemCreate, ItemResponse
from ..services.item_service import ItemService


router = APIRouter()
item_service = ItemService()


@router.get("/", response_model=list[ItemResponse])
async def read_items():
    return item_service.get_all_items()

@router.get("/{item_id}", response_model=ItemResponse)
async def read_item(item_id: int):
    item = item_service.get_item_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return item

@router.post("/", response_model=ItemResponse)
async def create_item(item: ItemCreate):
    if not item.name:
        raise HTTPException(status_code=400, detail="Name is required")

    new_id = len(item_service.repository.fake_db) + 1
    new_item = Item(id=new_id, **item.model_dump())
    return item_service.create_item(new_item)
