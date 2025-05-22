from pymongo import MongoClient

# Replace this with your actual connection string
connection_string = "mongodb+srv://roshan:roshanpwd@cluster0.uf1x9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)

# Access database and collection
db = client["dataa"]
collection = db["upload"]

# Sample data to insert
data = {
    "name": "Sabyasachi",
    "project": "Smart IoT Switch",
    "status": "Working"
}

# Insert the data
result = collection.insert_one(data)

# Print inserted ID
print("Inserted ID:", result.inserted_id)
