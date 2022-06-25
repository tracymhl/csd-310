from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.1sz6e.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
garrett = {
    "student_id": "1007",
    "first_name": "Garrett",
    "last_name": "Hiles",
}
dylan = {
    "student_id": "1008",
    "first_name": "Dylan",
    "last_name": "Sievers",
}
justin = {
    "student_id": "1009",
    "first_name": "Justin",
    "last_name": "Hilton",
}

garrett_student_id = db.student.insert_one(garrett).inserted_id
dylan_student_id = db.student.insert_one(dylan).inserted_id
justin_student_id = db.student.insert_one(justin).inserted_id
print(garrett_student_id)
print(dylan_student_id)
print(justin_student_id)

print(db.list_collection_names())
