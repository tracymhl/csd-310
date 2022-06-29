from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.1sz6e.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
student = db.student
student_list = student.find({})

print("\n --DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"]+ "\n")

test_doc = {
    "student_id": "1010",
    "first_name": "Finnegan",
    "last_name": "Francis"
}

test_doc_id = student.insert_one(test_doc).inserted_id

print("\n --INSERT STATEMENTS --")
print(" Inserted student record into the student collection with document_id " + str(test_doc_id))

student_test_doc = student.find_one({"student_id": "1010"})

print("\n --DISPLAYING STUDENT TEST DOC-- ")
print(" Student ID: " + student_test_doc["student_id"] + "\n First Name: " + student_test_doc["first_name"] + "\n Last Name: " + student_test_doc["last_name"] + "\n")

deleted_student_test_doc = student.delete_one({"student_id": "1010"})

new_student_list = student.find({})

print("\n --DISPLAYING STUDENT DOCUMENTS FROM find() QUERY-- ")

for doc in new_student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " + doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")

    
