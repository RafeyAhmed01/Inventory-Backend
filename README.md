# Inventory Backend

A simple inventory managament backend built with Python.

## Features

- View all products
- View a single product
- Add product
- Update product
- Delete product
- Persist data using JSON storage

## Tech Stack

- Python
- FastAPI
- JSON

## Project Structure

```
backend/
├── main.py 
├── services/
│   └── inventory.py
├── data/
│   └── db.json
```

## Installation

Clone the Repostory

```git clone <repo-url>```

```cd inventory-backend```

Install Dependencies

```uv sync```

 Run the Application

 ```uv run uvicorn main:app --reload```

 ##   API Endpoints

```
 Method	Endpoint	      Description
 GET	      /products	      Get all products
 GET	      /products/{id}      Get product by ID
 POST	      /products	      Add product
 PUT	      /products/{id}      Update product
 DELETE      /products/{id}      Delete product
```

## Storage 

Data is currently persistent in:

```data/data.json```


