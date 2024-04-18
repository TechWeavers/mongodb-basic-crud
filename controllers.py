from typing import List, Optional
from pydantic import BaseModel, ValidationError
import uuid
from db import create_mongodb_connection, insert_item_db, update_item_db, delete_item_db

class Item(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] = None
    price: float
    on_offer: bool = False

# Configurações de conexão com o MongoDB
connection_string = "mongodb://localhost:27017/"
database_name = "atividade-p1"
collection_name = "itens"

# Criando uma conexão com o MongoDB
db = create_mongodb_connection(connection_string, database_name)
collection = db[collection_name]

def create_item(item: Item) -> Item:
    item.id = str(uuid.uuid4())
    insert_item_db(collection, item.model_dump())
    return item

def get_all_items() -> List[Item]:
    items = []
    for item in collection.find():
        items.append(Item(**item))
    return items

def update_item(item_id: str, updated_item: Item) -> Optional[Item]:
    result = update_item_db(collection, item_id, updated_item.model_dump())
    if result:
        return updated_item
    return None

def delete_item(item_id: str) -> dict:
    result = delete_item_db(collection, item_id)
    return result
