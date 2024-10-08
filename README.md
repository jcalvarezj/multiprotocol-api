# multiprotocol-api

A proof of concept of a FastAPI backend that exposes endpoints working with different protocols (REST, SOAP)

```
multiprotocol-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── item_controller.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── item_service.py
│   ├── repositories/
│   │   ├── __init__.py
│   │   └── item_repository.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── item.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── item_schema.py
|   └── soap/
|       ├── __init__.py
|       └── item_controller.py
│
├── requirements.txt
└── README.md
```

## Install and Run

1. Clone the repository
2. Install dependencies on requirements.txt (virtual environment recommended)
3. Run using `uvicorn app.main:app --reload`


## REST Endpoints

### 1. Get all items

- **Method**: `GET`
- **Endpoint**: `/items/`
- **Description**: Retrieves all the currently stored items.
- **Response**:
  - **Status code**: `200 OK`
  - **Body**:
    ```json
    [
      {
        "id": 1,
        "name": "Item 1",
        "description": "Item 1 description"
      },
      {
        "id": 2,
        "name": "Item 2",
        "description": "Item 2 description"
      }
    ]
    ```

### 2. Create new item

- **Method**: `POST`
- **Endpoint**: `/items/`
- **Description**: Creates a new item with a name and a description.
- **Request body**:
  - **Type**: `application/json`
  - **Example**:
    ```json
    {
      "name": "New Item",
      "description": "New item description"
    }
    ```
- **Response**:
  - **Status code**: `201 Created`
  - **Body**:
    ```json
    {
      "id": 3,
      "name": "New Item",
      "description": "New item description"
    }
    ```
  - **Status code**: `400 Bad Request` (for incorrect input request bodies)
  - **Body**:
    ```json
    {
      "detail": "Name is required"
    }
    ```

### 3. Get item by ID

- **Method**: `GET`
- **Endpoint**: `/items/{item_id}`
- **Description**: Returns a specific item given its ID.
- **Path parameters**:
  - `item_id` (int): The ID of the item to retrieve.
- **Response**:
  - **Status code**: `200 OK`
  - **Body**:
    ```json
    {
      "id": 1,
      "name": "Item 1",
      "description": "Item 1 description"
    }
    ```
  - **Status code**: `404 Not Found` (if the item is not found)
  - **Body**:
    ```json
    {
      "detail": "Item not found"
    }
    ```

## SOAP Endpoints

### 1. Create new item

- **Method**: `POST`
- **Endpoint**: `/items/`
- **Description**: Creates a new item with a name and a description.
- **Request body**:
  - **Type**: `text/xml`
  - **Example**:
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <CreateItem xmlns="http://example.com/soap/items">
                <Item>
                    <name>Item 1</name>
                    <description>Item de prueba</description>
                </Item>
            </CreateItem>
        </soap:Body>
    </soap:Envelope>
    ```
- **Response**:
  - **Status code**: `201 Created`
  - **Body**:
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <CreateItemResponse xmlns="http://example.com/soap/items">
                <Item>
                    <id>3</id>
                    <name>New Item</name>
                    <description>New item description</description>
                </Item>
            </CreateItemResponse>
        </soap:Body>
    </soap:Envelope>
    ```
  - **Status code**: `400 Bad Request` (for incorrect input request bodies)
  - **Body**:
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <Fault>
                <faultcode>soap:Client</faultcode>
                <faultstring>Name is required</faultstring>
                <faultstring>Error message</faultstring>
                <statusCode>400</statusCode>
                <request>
                    <method>{Request method}</method>
                    <url>{Request URL}</url>
                    <headers>
                        {Request headers}
                    </headers>
                    <body>{Request body}</body>
                </request>
            </Fault>
        </soap:Body>
    </soap:Envelope>
    ```

### 2. Get all items

- **Method**: `GET`
- **Endpoint**: `/items/`
- **Description**: Retrieves all the currently stored items.
- **Response**:
  - **Status code**: `200 OK`
  - **Body**:
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <GetItemsResponse xmlns="http://example.com/soap/items">
                <Items>
                    <Item>
                        <id>1</id>
                        <name>Item 1</name>
                        <description>Item 1 description</description>
                    </Item>
                    <Item>
                        <id>2</id>
                        <name>Item 2</name>
                        <description>Item 2 description</description>
                    </Item>
                </Items>
            </GetItemsResponse>
        </soap:Body>
    </soap:Envelope>
    ```

### 3. Get item by ID

- **Method**: `GET`
- **Endpoint**: `/items/{item_id}`
- **Description**: Returns a specific item given its ID.
- **Path parameters**:
  - `item_id` (int): The ID of the item to retrieve.
- **Response**:
  - **Status code**: `200 OK`
  - **Body**:
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <GetItemResponse xmlns="http://example.com/soap/items">
                <Item>
                    <id>1</id>
                    <name>Item 1</name>
                    <description>Item 1 description</description>
                </Item>
            </GetItemResponse>
        </soap:Body>
    </soap:Envelope>
    ```
  - **Status code**: `404 Not Found` (if the item is not found)
  - **Body**:
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <Fault>
                <faultcode>soap:Client</faultcode>
                <faultstring>Item not found</faultstring>
                <faultstring>Error message</faultstring>
                <statusCode>404</statusCode>
                <request>
                    <method>{Request method}</method>
                    <url>{Request URL}</url>
                    <headers>
                        {Request headers}
                    </headers>
                    <body>{Request body}</body>
                </request>
            </Fault>
        </soap:Body>
    </soap:Envelope>
    ```
