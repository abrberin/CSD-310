from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.rv83ky7.mongodb.net/?retryWrites=true&w=majority")
db = client.pytech
students = db.students
print("All Students:")
all_students = students.find({})
for student in all_students:
    print(student)
student_id_to_find = 1007
print(f"\nStudent with student_id {student_id_to_find}:")
found_student = students.find_one({"student_id": student_id_to_find})
if found_student:
    print(found_student)
else:
    print(f"No student found with student_id {student_id_to_find}")
client.close()
