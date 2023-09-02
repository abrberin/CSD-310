from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.rv83ky7.mongodb.net/?retryWrites=true&w=majority"
connection_string = "mongodb+srv://admin:admin@cluster0.rv83ky7.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
try:
    client = MongoClient(connection_string)

    print("--Pytech COllection List--")
    print(db.list_collection_names())

    client.close()
except Exception as e:
    # Print an error message if there's an issue with the connection
    print(f"Error: {e}")