import pymongo

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://deepjyoti:Snape%401993@cluster0.jmolyan.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client.test
print(db)

d = {
    "name":"deepjyoti",
    "emailid":"deep@gmail.com",
    "surname":"bhattacharjee"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)