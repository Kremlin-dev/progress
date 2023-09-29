import pymongo
#connecting to the database
conn = "mongodb+srv://Kremlin:ch5BDbt8xwWLL59f@cluster0.7o0xg5b.mongodb.net/?retryWrites=true&w=majority"
try:
    client = pymongo.MongoClient(conn)
    print("Connection successful")
except Exception:
    print("Connection failed with error")

#creating a database
db =client["Pymongodb"]

# #After creating a database, we create a collection
mycollection = db["firstcollection"]

mydoc={
     "name":"Isaac",
     "age": 34
 }

res= mycollection.insert_one(mydoc)

print(client.list_database_names())