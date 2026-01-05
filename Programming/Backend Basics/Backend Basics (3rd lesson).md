---
type: note
status: done
tags: ['tech/backend']
sources:
- "[[Backend Basics Course]]"
authors:
-
---

#🃏/semantic/backend #🃏/backend-basics-course

**Codewords:** FastAPI, Pydantic, Uvicorn, API Endpoint, Path Operation, Path Parameter, Query Parameter, Request Body.

## 1. Introduction to FastAPI

FastAPI is a modern, high-performance web framework for building APIs with Python. It's built on top of `asyncio` and is one of the fastest Python frameworks available.

**Key Features:**

To get started, you need to install `fastapi` and an ASGI server, such as `uvicorn`.

```bash
pip install fastapi "uvicorn[standard]"
```

## 2. Your First API

Create a file named `main.py`:

```python
from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a "path operation decorator"
@app.get("/")
async def read_root():
 # This is the function that will be called when a client
 # makes a GET request to the root URL ("/")
 return {"Hello": "World"}

```

**Run the server:**
Open your terminal and run:
```bash
uvicorn main:app --reload
```

Now, open your browser and go to `http://127.0.0.1:8000`. You will see `{"Hello":"World"}`.
Also, go to `http://127.0.0.1:8000/docs`. You will see the automatic interactive API documentation.

## 3. Path and Query Parameters

You can declare parameters that are part of the URL path or passed in the query string.

### Path Parameters
Declare them using f-string-like syntax in the path. They are passed as arguments to your function.

```python
# In main.py
@app.get("/items/{item_id}")
async def read_item(item_id: int):
 return {"item_id": item_id}
```
Now go to `http://127.0.0.1:8000/items/5`. FastAPI validates that `item_id` is an integer.

### Query Parameters
Parameters that are not part of the path are automatically interpreted as query parameters.

```python
# In main.py
# A fake database of items
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
 return fake_items_db[skip : skip + limit]
```
Now go to `http://127.0.0.1:8000/items/?skip=0&limit=2`.

## 4. Request Body and Pydantic

When you need the client to send data (e.g., with a `POST` request), you declare it as a **Request Body**. To define the structure of the body, you use **Pydantic** models.

```python
# In main.py
from pydantic import BaseModel

class Item(BaseModel):
 name: str
 description: str | None = None # This field is optional
 price: float
 tax: float | None = None

@app.post("/items/")
async def create_item(item: Item):
 item_dict = item.dict()
 # You can add logic here to save the item to a database
 return item_dict
```
With this, FastAPI will:
1. Read the body of the request as JSON.
2. Validate that it has a `name`, `price`, and optionally `description` and `tax`.
3. Convert the types if needed.
4. Pass the validated data as the `item` parameter.
You can test this in the `/docs` page.

**Practice Problem: To-Do List API**

Build a simple API for managing a to-do list. For now, the "database" can just be a Python dictionary in your `main.py`.

**Requirements:**
1. Create a Pydantic model for a `Todo` item. It should have `id` (int), `title` (str), and `completed` (bool, with a default of `False`).
2. Store the todos in a dictionary where the key is the todo's ID.
3. Implement the following endpoints:
 - `POST /todos/`: Create a new todo. It should automatically assign a new ID. The request body will contain the `title`.
 - `GET /todos/`: Get a list of all todos.
 - `GET /todos/{todo_id}`: Get a single todo by its ID.
 - `PUT /todos/{todo_id}`: Mark a todo as completed.
 - `DELETE /todos/{todo_id}`: Delete a todo.

---

**Key Questions:**

1. What is FastAPI, and what are two of its main advantages?
?
- FastAPI is a modern, high-performance web framework for building APIs in Python.
- **Advantages:** It's very fast (high performance) and provides automatic interactive documentation.

2. What is the difference between a path parameter and a query parameter?
?
- A **path parameter** is part of the URL path itself, used to identify a specific resource (e.g., `/users/123`).
- A **query parameter** is a key-value pair appended to the URL after a `?`, used for filtering, sorting, or pagination (e.g., `/items?limit=10`).

3. What is Pydantic's role in FastAPI?
?
- Pydantic is used for data validation and settings management. In FastAPI, you use Pydantic models to define the expected structure and data types of request bodies, ensuring the incoming data is valid before your code processes it.

4. What command do you use to run a FastAPI application?
?
- `uvicorn main:app --reload`, where `main` is the Python file and `app` is the FastAPI instance. 