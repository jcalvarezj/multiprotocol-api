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
│   └── schemas/
│       ├── __init__.py
│       └── item_schema.py
│
├── requirements.txt
└── README.md
```

## Install and Run

1. Clone the repository
2. Install dependencies on requirements.txt (virtual environment recommended)
3. Run using `uvicorn app.main:app --reload`


## Endpoints

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
