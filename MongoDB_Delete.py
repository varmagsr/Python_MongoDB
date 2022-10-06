
import certifi as certifi
from bson import ObjectId
from pymongo import MongoClient

## below link is usefull for certificate error
## https://stackoverflow.com/questions/68123923/pymongo-ssl-certificate-verify-failed-certificate-verify-failed-unable-to-ge

client = MongoClient("mongodb+srv://username:password@prodvpc.vzgw8fc.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=certifi.where())
print(client.list_database_names())

db = client["sample_airbnb"]
print(db.list_collection_names())

collection = db["listingsAndReviews"]


# --------------------------------------------------------------------------------------------------------------------
#   DELETE OPERATION IN MONGODB CRUD.
# --------------------------------------------------------------------------------------------------------------------
collection.delete_one({"name":"Bhimavaram Palace"})



