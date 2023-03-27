import json
with open('test.json', 'r') as f:
    data = json.load(f)

print(data)

# Append the new data to the dictionary
new_data = {"datatype": "example", "value": "123", "scope": "test"}
data["a"].append(new_data)

# Write the updated dictionary back to the JSON file
with open('data.json', 'w') as f:
    json.dump(data, f)