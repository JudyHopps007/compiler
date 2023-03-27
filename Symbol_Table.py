
import json
# Data to be written
dictionary ={
    'IDENTIFIER' : 'guest_name',
    'DATA_TYPE' : 'guest_phone_number',
    'VALUE' : 'guest_email',
    'SCOPE' : 'dguest_room_type'
}

with open('test.json') as json_file:
    data = json.load(json_file)
"""
temp = data['Symbol_table']
temp.append(dictionary)
with open('test.json', 'w') as json_file_write:
   json.dump(data,json_file_write, indent=4)
"""


temp =  data['Symbol_table']

print(temp)

print(len(temp))

