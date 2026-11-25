# load_inventory
# save_inventory
# get_products
# get_product
# add_product
# update_product
# delete_product
import json


def get_inventory_data():
    inventory = load_inventory()
    if inventory is None:
        return []
    return inventory

# ############################### #

def get_products():
    inventory = get_inventory_data()
    return inventory


def get_product(id):
    inventory = get_inventory_data()
    if id is None:
        return None
    for product in inventory:
        if id == product['id']:
            return product
    else:
        return None


def add_product(new_product):
    """
    {id: 1, product: {}}
    """
    inventory = get_inventory_data()
    # validation
    new_product = new_product.model_dump()
    if not new_product:
        return
    new_product['id'] = inventory[-1]['id'] + 1 if inventory else 0
    inventory.append(new_product)
    save_inventory(inventory)
    return new_product


def update_product(id, new_product):
    inventory = get_inventory_data()
    new_product = new_product.model_dump()
    if id is None:
        return
    for product in inventory:
        if product['id'] == id:
            product.update(new_product)
            save_inventory(inventory)
            new_product['id'] = id
            return new_product
    else:
        print(f"Product with id: {id} not found.")
        return



def delete_product(id):
    inventory = get_inventory_data()
    if id is None:
        return
    for product in inventory:
        if product['id'] == id:
            selected_product = product
            inventory.remove(product)
            save_inventory(inventory)
            return selected_product
    else:
        print(f"Product with id: {id} not found.")
        return

def load_inventory():
    try:
        with open('data/db.json', 'r') as file:
            data = json.load(file)
            return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(e)

def save_inventory(new_inventory):
    try:
        with open('data/db.json', 'w') as file:
            json.dump(new_inventory, file, indent=2)
    except PermissionError as e:
        print(e)
