from pymongo import MongoClient
mongo_uri='mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client=MongoClient(mongo_uri)
pilot_app=client.c4e
services=pilot_app['posts']
mypost={
    'title':'TOT',
    'author':'NTĐ',
    'content':'hự hự'
}
services.insert_one(mypost)