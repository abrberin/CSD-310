from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.rv83ky7.mongodb.net/?retryWrites=true&w=majority")
db = client.pytech
students = db.students
student1 = {
    "student_id": 1007,
    "first_name": "Sarah",
    "last_name": "Jake"
}
student2 = {
    "student_id": 1008,
    "first_name": "Merz",
    "last_name": "Silvo"
}
student3 = {
    "student_id": 1009,
    "first_name": "Jerac",
    "last_name": "Pat"
}
student1_id = students.insert_one(student1).inserted_id
student2_id = students.insert_one(student2).inserted_id
student3_id = students.insert_one(student3).inserted_id
print(f"Inserted Student 1 with ID: {student1_id}")
print(f"Inserted Student 2 with ID: {student2_id}")
print(f"Inserted Student 3 with ID: {student3_id}")
client.close()
