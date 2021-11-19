""" 
    Title: pytech_update.py
    Author: Avery Owen
    Date: 18 November 2021
    Description: Updating documents in the Pytech database.
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

# update student 1007's last name
update = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Oakenshield Jr"}})

# find updated student 1007 document
thorin = students.find_one({"student_id": "1007"})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FOR STUDENT 1007 --")

# output updated student document
print("  Student ID: " + thorin["student_id"] + "\n  First Name: " + thorin["first_name"] + "\n  Last Name: " + thorin["last_name"] + "\n")

# exit message 
input("\n\n  End of program, press any key to continue...")
