from pymongo import MongoClient
mongo_uri='mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client=MongoClient(mongo_uri)
pilot_app=client.c4e
services=pilot_app['posts']
mypost={
    'title':'404_noT_FOuNd',
    'author':'NTĐ',
    'content':'những lúc như này cần một nụ cười thật tươi'
}
services.insert_one(mypost)