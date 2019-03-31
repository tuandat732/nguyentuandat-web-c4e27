from mlab import all_river
for i in all_river:
    if i['continent'] == 'Africa':
        print(i['name'])