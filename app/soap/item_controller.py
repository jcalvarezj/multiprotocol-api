import xmltodict
from fastapi import APIRouter, Response, Request

from ..models.item import Item
from ..schemas.item_schema import ItemResponse
from ..services.item_service import ItemService
from ..exceptions.handlers import SOAPException


router = APIRouter()
item_service = ItemService()

@router.get("/items", response_class=Response)
async def get_items_xml():
    items_xml = """<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <GetItemsResponse xmlns="http://example.com/soap/items">
                <Items>"""

    for item in item_service.get_all_items():
        items_xml += f"""
                    <Item>
                        <id>{item.id}</id>
                        <name>{item.name}</name>
                        <description>{item.description}</description>
                    </Item>"""

    items_xml += """
                </Items>
            </GetItemsResponse>
        </soap:Body>
    </soap:Envelope>"""

    return Response(content=items_xml, media_type="text/xml")

@router.get("/items/{item_id}", response_class=Response)
async def get_item_by_id(item_id: int):
    item = item_service.get_item_by_id(item_id)

    if item is None:
        raise SOAPException("Item not found", status_code=404)

    response_data = {
        "soap:Envelope": {
            "@xmlns:soap": "http://schemas.xmlsoap.org/soap/envelope/",
            "soap:Body": {
                "GetItemResponse": {
                    "@xmlns": "http://example.com/soap/items",
                    "Item": item.model_dump()
                }
            }
        }
    }

    response_xml = xmltodict.unparse(response_data, pretty=True)
    return Response(content=response_xml, media_type="text/xml")

@router.post("/items", response_model=ItemResponse)
async def create_item(request: Request):
    xml_body = await request.body()
    try:
        data_dict = xmltodict.parse(xml_body)
        item_data = data_dict['soap:Envelope']['soap:Body']['CreateItem']['Item']

        new_id = len(item_service.repository.fake_db) + 1
        new_item = item_service.create_item(Item(id=new_id, **item_data))

        response_dict = {
            "soap:Envelope": {
                "@xmlns:soap": "http://schemas.xmlsoap.org/soap/envelope/",
                "soap:Body": {
                    "CreateItemResponse": {
                        "@xmlns": "http://example.com/soap/items",
                        "Item": new_item.model_dump()
                    }
                }
            }
        }
        response_xml = xmltodict.unparse(response_dict, pretty=True)

        return Response(content=response_xml, media_type="text/xml", status_code=201)
    except Exception as e:
        raise SOAPException(f"Error processing XML: {type(e).__name__} - {str(e)}",
                            status_code=400, request_body=xml_body.decode())
