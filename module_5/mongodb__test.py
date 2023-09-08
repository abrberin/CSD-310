import pymongo
from pymongo import MongoClient
Client = MongoClient("mongodb+srv://admin:admin@cluster0.rv83ky7.mongodb.net/?retryWrites=true&w=majority")
db = Client["pytech"]
print(db.list_collection_names)