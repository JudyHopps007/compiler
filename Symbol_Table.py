"""
import json
# Data to be written
dictionary ={
    'IDENTIFIER' : None,
    'DATA_TYPE' : 'guest_phone_number',
    'VALUE' : 'guest_email',
    'SCOPE' : 'dguest_room_type'
}

with open('test.json') as json_file:
    data = json.load(json_file)

temp = data['Symbol_table']
temp.append(dictionary)
with open('test.json', 'w') as json_file_write:
   json.dump(data,json_file_write, indent=4)



temp =  data['Symbol_table']

print(temp)
for i in range(len(temp)):
    print(data['Symbol_table'][i]['IDENTIFIER'])
    data['Symbol_table'][i]['IDENTIFIER'] = '34'
"""
import json

data = {"Symbol_table": []}

# Open the JSON file in write mode and write the empty object to it
with open("test.json", 'w') as f:
    json.dump(data, f)