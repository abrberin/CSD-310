import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.rv83ky7.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
collection = db["students"]

find = {"_id" : 1010}
collection.delete_one(find)