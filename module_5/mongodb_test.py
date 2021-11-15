from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.vwpot.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(url,  tls=True, tlsAllowInvalidCertificates=True)

db = client.pytech
print(db.list_collection_names())

