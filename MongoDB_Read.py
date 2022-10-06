import certifi as certifi
from bson import ObjectId
from pymongo import MongoClient



client = MongoClient("mongodb+srv://username:password@prodvpc.vzgw8fc.mongodb.net/?retryWrites=true&w=majority",
                     tlsCAFile=certifi.where())
print(client.list_database_names())

db = client["sample_airbnb"]
print(db.list_collection_names())

collection = db["listingsAndReviews"]
# --------------------------------------------------------------------------------------------------------------------
#   READ OPERATION IN MONGODB CRUD.
# --------------------------------------------------------------------------------------------------------------------
# print(collection.index_information())
# Below are 4 different ways to read the documents from MongoDB collections
# 1. find_one() will print the first record in the collection
print(collection.find_one())

# 2. find() will give the courser pointer back, in generally it will point to first record in the collection documents.
# we can iterate though list of collections using courser.
record = collection.find()
print(record.next())

# 3 & 4 are the iteration example for the courser and filtering the documents in the collections.
for i in collection.find({"_id": "10021707"}):
    print(i)

for x in collection.find(
        {"minimum_nights": "1", "bedrooms": 1, "accommodates": 2, "maximum_nights": "1125", "property_type": "Hostel",
         "bathrooms": 1.5}):
    print(x)
