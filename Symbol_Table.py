
import json
# Data to be written
dictionary ={
    'Guest_name' : 'guest_name',
    'Guest_Phone' : 'guest_phone_number',
    'Guest_Email' : 'guest_email',
    'Guest_room' : 'dguest_room_type'
}

with open('test.json') as json_file:
    data = json.load(json_file)

temp = data['Guests']
temp.append(dictionary)
with open('test.json', 'w') as json_file_write:
   json.dump(data,json_file_write, indent=4)
