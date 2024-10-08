from fastapi import FastAPI, Request

from .soap.item_controller import router as item_soap_router
from .controllers.item_controller import router as item_router
from app.exceptions.handlers import soap_exception_handler, SOAPException


app = FastAPI()

@app.exception_handler(SOAPException)
async def custom_soap_exception_handler(request: Request, exc: SOAPException):
    return await soap_exception_handler(request, exc)

app.include_router(item_router, prefix="/items", tags=["items"])
app.include_router(item_soap_router, prefix="/soap", tags=["items_soap"])
