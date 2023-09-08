import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.rv83ky7.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
collection = db["students"]
post1 = {
    "_id": 1007,
    "first_name": "Sarah",
    "last_name": "Jake"
}
post2 = {
    "_id": 1008,
    "first_name": "Merz",
    "last_name": "Silvo"
}
post3 = {
    "_id": 1009,
    "first_name": "Jerac",
    "last_name": "Pat"
}

collection.insert_many([post1, post2, post3])

