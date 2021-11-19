""" 
    Title: pytech_delete.py
    Author: Avery Owen
    Date: 18 November 2021
    Description: Delete documents from an existing MongoDB connection.
"""

""" import statements """
from pymongo import MongoClient

# MongoDB connection string 
url = "mongodb+srv://admin:admin@cluster0.vwpot.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
# create client

# connect to the MongoDB cluster 
client = MongoClient(url,  tls=True, tlsAllowInvalidCertificates=True)

# connect pytech database
db = client.pytech

# get the students collection 
students = db.students

# find all students in the collection 
student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# insert new document
new_doc = {
    "student_id": "1010",
    "first_name": "Avery",
    "last_name": "Owen"
}    

# instert new document into MongoDB
new_doc_id = students.insert_one(new_doc).inserted_id

# insert statements with output 
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(new_doc_id))

# call find_one for student 1010
student_new_doc = students.find_one({"student_id": "1010"})

# output results 
print("\n  -- DISPLAYING STUDENT TEST DOC -- ")
print("  Student ID: " + student_new_doc["student_id"] + "\n  First Name: " + student_new_doc["first_name"] + "\n  Last Name: " + student_new_doc["last_name"] + "\n")

# call delete one method to remove student new doc
deleted_student_new_doc = students.delete_one({"student_id": "1010"})

# find all students in collection
new_student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in new_student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")

