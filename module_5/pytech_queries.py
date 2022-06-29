from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.1sz6e.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

#docs = db.pytech.students.find({})
students = db.students
student_list = students.find({})
print("\n -- Displaying Students Documents from find() Query --")


for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

garrett = students.find_one({"student_id": "1007"})

print("\n  -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + garrett["student_id"] + "\n  First Name: " + garrett["first_name"] + "\n  Last Name: " + garrett["last_name"] + "\n")


