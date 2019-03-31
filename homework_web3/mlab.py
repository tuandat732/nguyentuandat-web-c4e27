from pymongo import MongoClient
mongo_uri='mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client=MongoClient(mongo_uri)
database=client.c4e
co_river=database['river']
all_river=co_river.find()
