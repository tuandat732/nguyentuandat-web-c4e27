from pymongo import MongoClient
from bson.objectid import ObjectId
bike_uri='mongodb+srv://admin:admin@cluster0-jrxnz.mongodb.net/test?retryWrites=true'
bike_client=MongoClient(bike_uri)
bike_base=bike_client.bike
all_bike=bike_base['all-bike']
