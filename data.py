from pymongo import MongoClient
from pymongo.errors import PyMongoError
import pprint

def connect_to_mongodb(connection_string):
    return MongoClient(connection_string)

def fetch_existing_documents(collection):
    print("Existing documents:")
    for doc in collection.find():
        pprint.pprint(doc)

def watch_new_inserts(collection, on_insert=None):
    """
    Watches the collection for new inserts.
    If `on_insert` is provided, it is called with the inserted document.
    """
    try:
        print("\nWatching for new inserts...")
        with collection.watch([{'$match': {'operationType': 'insert'}}]) as stream:
            for change in stream:
                full_doc = change['fullDocument']
                print("\n📦 New data added:")
                pprint.pprint(full_doc)
                
                if on_insert:
                    on_insert(full_doc)
    except PyMongoError as e:
        print("Error watching the collection:", e)

def main():
    connection_string = "mongodb+srv://roshan:roshanpwd@cluster0.uf1x9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = connect_to_mongodb(connection_string)

    db = client["test"]
    collection = db["dataas"]

    fetch_existing_documents(collection)
    watch_new_inserts(collection)

# Run only if this file is directly executed
if __name__ == "__main__":
    main()
