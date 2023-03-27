import json
with open('test.json', 'r') as f:
    data = json.load(f)

print(data)

data['new_key'] = 'new_value'

with open('data.json', 'w') as f:
    json.dump(data, f)