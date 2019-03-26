from pymongo import MongoClient
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
all_doc=first_collection.find() #tìm ra tất cả các dic có trong()
for doc in all_doc:
    print(doc)
    print(doc['title'])
#6.2 read one
one_doc=first_collection.find_one({'title':'lol'}) #phải tìm theo dạng dic
print(one_doc)
 

