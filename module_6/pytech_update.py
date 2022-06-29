from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.1sz6e.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
student = db.student
student_list = student.find({})

print("\n -- DISPLAYING STUDENTS IN DOCUMENTS FROM find() QUERY -- ")

for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

result = student.update_one({"student_id": "1007"}, {"$set": {"last_name": "Bader"}})

garrett = student.find_one({"student_id": "1007"})

print("\n -- DISPLAYING STUDENT DOCUMENT 1007 --")

print(" Student ID: " + garrett["student_id"] + "\n First Name: " + garrett["first_name"] + "\n Last Name: " + garrett["last_name"] + "\n")
