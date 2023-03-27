import json
with open('test.json', 'r') as f:
    data = json.load(f)
import json
# Data to be written
dictionary ={
  "id": "04",
  "name": "sunil",
  "department": "HR"
}
# Serializing json
json_object = json.dumps(dictionary, indent = 4)
print(json_object)
