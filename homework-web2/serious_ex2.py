from pymongo import MongoClient
from matplotlib import pyplot

mongo_uri='mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client=MongoClient(mongo_uri)
pilot_app=client.c4e
services=pilot_app['customers']
all_cus=services.find()
b={}
dem=0
for i in all_cus:
    m=i['ref']
    if m in b: b[m]+=1
    else: b[m]=1
    dem+=1
data=[]
name=[]
for i,j in b.items():
    data.append(j)
    name.append(i)
pyplot.pie(data, labels=name , autopct='%.2f%%', explode=[0,0.1,0],colors=['red','blue','yellow'])
pyplot.title('% Customers group by REFS', fontsize=24,color='red')
pyplot.show()

