from pymongo import MongoClient
from bson.objectid import ObjectId
#b1: connect mongodb
mongo_uri='mongodb+srv://admin:admin@cluster0-jrxnz.mongodb.net/test?retryWrites=true'
client=MongoClient(mongo_uri)

#2: get/create database
db_demo = client.test_database #tạo database tên là test_database

#3: get/create collection
first_collection=db_demo['my_collection']

#4: create document
# game_document={
#     "title":"fo4",
#     "description":'fifa online 4'
# }

#5: insert document
# first_collection.insert_one(game_document)

### READ
#6.1: read all
# all_doc=first_collection.find() #tìm ra tất cả các dic có trong()
# for doc in all_doc:
#     print(doc)
#     print(doc['title'])
#6.2 read one
# one_doc=first_collection.find_one({'title':'lol'}) #phải tìm theo dạng dic
# print(one_doc)

#7: DELETE
# del_doc = first_collection.find_one({'_id':ObjectId('5c979bff54c5580e0cb933da')})
# if del_doc != None:
#     first_collection.delete_one(del_doc)
# else: print('not found')

#8: UPDATE
#8.1 find
update_doc=first_collection.find_one({'_id':ObjectId('5c979c1e54c558456c215fa1')})
new_value={'$set':{'title':'game'}}
first_collection.update_one(update_doc,new_value)



