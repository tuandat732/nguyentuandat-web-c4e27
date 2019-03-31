from mlab import all_river
for i in all_river:
    if i['continent'] == 'S. America' and i['length'] <= 1000:
        print(i['name'])