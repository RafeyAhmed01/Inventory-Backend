from fastapi import FastAPI, status

from schemas import ProductCreate, ProductResponse
from services.inventory import (
    add_product,
    delete_product,
    get_product,
    get_products,
    update_product,
)

app = FastAPI()

@app.get('/')
def root():
    return {
        "message": "Welcome User!"
    }

@app.get('/products')
def show_products():
    return get_products()

@app.get('/product/{id}')
def show_product(id: int):
    return get_product(id)

@app.post('/product', response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product: ProductCreate):
    return add_product(product)

@app.put('/product/{id}', response_model=ProductResponse)
def modify_product(id: int, new_product: ProductCreate):
    return update_product(id, new_product)

@app.delete('/product/{id}', response_model=ProductResponse)
def remove_product(id: int):
    return delete_product(id)
