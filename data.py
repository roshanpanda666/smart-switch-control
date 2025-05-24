from pymongo import MongoClient
from pymongo.errors import PyMongoError
from dotenv import load_dotenv
import pprint
import os

# Load environment variables from .env file
load_dotenv()

def connect_to_mongodb(connection_string):
    return MongoClient(connection_string)

def fetch_existing_documents(collection):
    print("📄 Existing documents:")
    for doc in collection.find():
        pprint.pprint(doc)

def watch_new_inserts(collection, on_insert=None):
    """
    Watches the collection for new inserts.
    If `on_insert` is provided, it is called with the inserted document.
    """
    try:
        print("\n👀 Watching for new inserts...")
        with collection.watch([{'$match': {'operationType': 'insert'}}]) as stream:
            for change in stream:
                full_doc = change['fullDocument']
                print("\n📦 New data added:")
                pprint.pprint(full_doc)
                
                if on_insert:
                    on_insert(full_doc)
    except PyMongoError as e:
        print("❌ Error watching the collection:", e)

def main():
    connection_string = os.getenv("MONGO_URI")
    if not connection_string:
        print("❌ MONGO_URI not set in .env")
        return

    client = connect_to_mongodb(connection_string)

    db = client["test"]
    collection = db["dataas"]

    fetch_existing_documents(collection)
    watch_new_inserts(collection)

# Run only if this file is directly executed
if __name__ == "__main__":
    main()
