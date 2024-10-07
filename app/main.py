from fastapi import FastAPI
from .controllers.item_controller import router as item_router

app = FastAPI()

app.include_router(item_router, prefix="/items", tags=["items"])
