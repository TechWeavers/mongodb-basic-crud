from pymongo import MongoClient

def create_mongodb_connection(connection_string, database_name):
    client = MongoClient(connection_string)
    db = client[database_name]
    return db

def insert_item_db(collection, item):
    result = collection.insert_one(item)
    print("Item inserted with id:", result.inserted_id)

def update_item_db(collection, item_id, updated_item):
    updated_item["id"] = item_id
    result = collection.update_one({"id": item_id}, {"$set": updated_item})
    if result.modified_count > 0:
        print("Item updated successfully")
    else:
        print("No item found with the provided ID")

def delete_item_db(collection, item_id):
    result = collection.delete_one({"id": item_id})
    if result.deleted_count > 0:
        print("Item deleted successfully")
    else:
        print("No item found with the provided ID")

