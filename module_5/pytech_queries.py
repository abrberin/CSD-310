import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.rv83ky7.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
collection = db["students"]

results = collection.find({"_id":1007})
for x in results:
    print(x)