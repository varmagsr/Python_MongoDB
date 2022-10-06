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
#   WRITE/CREATE OPERATION IN MONGODB CRUD.
# --------------------------------------------------------------------------------------------------------------------
collection.insert_one({

  "listing_url": "https://www.airbnb.com/rooms/24170111",
  "name": "Bhimavaram Palace",
  "summary": "you will Rock",
  "space": "enjoy every thing",
  "description": "you will be happy here..",
  "neighborhood_overview": "running tracks",
  "notes": "abcdef",
  "transit": "train bus",
  "access": "key are ready",
  "interaction": "for each bed its 20$",
  "house_rules": "no rules",
  "property_type": "Hostel",
  "room_type": "Private room",
  "bed_type": "Real Bed",
  "minimum_nights": "1",
  "maximum_nights": "1125",
  "cancellation_policy": "flexible",
  "last_scraped": {
    "$date": {
      "$numberLong": "1550466000000"
    }
  },
  "calendar_last_scraped": {
    "$date": {
      "$numberLong": "1550466000000"
    }
  },
  "accommodates": 2,
  "bedrooms": 1,
  "beds": 1,
  "number_of_reviews": 0,
  "bathrooms": {
    "$numberDecimal": "1.5"
  },
  "amenities": [
    "TV",
    "Wifi",
    "Kitchen",
    "Smoking allowed",
    "Gym",
    "Breakfast",
    "Free street parking",
    "Heating",
    "Suitable for events",
    "Washer",
    "Dryer",
    "Safety card",
    "Essentials",
    "Shampoo",
    "Lock on bedroom door",
    "Hangers",
    "Hair dryer",
    "Iron",
    "Laptop friendly workspace",
    "Self check-in",
    "Building staff",
    "Hot water",
    "Bed linens",
    "Extra pillows and blankets",
    "Microwave",
    "Coffee maker",
    "Refrigerator",
    "Dishes and silverware",
    "Cooking basics",
    "Oven",
    "Stove",
    "Patio or balcony",
    "Beach essentials",
    "Long term stays allowed"
  ],
  "price": {
    "$numberDecimal": "143.00"
  },
  "extra_people": {
    "$numberDecimal": "0.00"
  },
  "guests_included": {
    "$numberDecimal": "1"
  },
  "images": {
    "thumbnail_url": "",
    "medium_url": "",
    "picture_url": "https://a0.muscache.com/im/pictures/d3c8e1be-b8fb-4319-9832-ee534aded375.jpg?aki_policy=large",
    "xl_picture_url": ""
  },
  "host": {
    "host_id": "182163308",
    "host_url": "https://www.airbnb.com/users/show/182163308",
    "host_name": "Rajesh",
    "host_location": "TR",
    "host_about": "",
    "host_thumbnail_url": "https://a0.muscache.com/im/pictures/user/d48996ff-e916-4b31-bce0-f4caab708660.jpg?aki_policy=profile_small",
    "host_picture_url": "https://a0.muscache.com/im/pictures/user/d48996ff-e916-4b31-bce0-f4caab708660.jpg?aki_policy=profile_x_medium",
    "host_neighbourhood": "",
    "host_is_superhost": False,
    "host_has_profile_pic": True,
    "host_identity_verified": False,
    "host_listings_count": 1,
    "host_total_listings_count": 1,
    "host_verifications": [
      "phone"
    ]
  },
  "address": {
    "street": "Okmeydanı, İstanbul, Turkey",
    "suburb": "Beyoglu",
    "government_area": "Beyoglu",
    "market": "Istanbul",
    "country": "Turkey",
    "country_code": "TR",
    "location": {
      "type": "Point",
      "coordinates": [
        28.95901,
        41.05187
      ],
      "is_location_exact": False
    }
  },
  "availability": {
    "availability_30": 29,
    "availability_60": 59,
    "availability_90": 89,
    "availability_365": 179
  },
  "review_scores": {},
  "reviews": []


})
