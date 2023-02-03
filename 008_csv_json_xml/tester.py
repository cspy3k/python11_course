import json
json_string ='''{
  "people": [
    {
      "name": "Jack Sumers",
      "phone": "555-555-555",
      "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
      "has_licence": false,
      "salary": 1500
    },
    {
      "name": "Mary Smith",
      "phone": "777-777-777",
      "emails": null,
      "has_licence": true,
      "salary": 1700
    },
    {
      "name": "Steven Cooke",
      "phone": null,
      "emails": "stevencooke@example.com",
      "has_licence": true,
      "salary": 2500
    }
  ]
}'''

data = json.loads(json_string)
# print(data)
# print(type(data))
# print(data['people'][0]['name'])

print(data)
data['people'][0]['name'] = 'Bob Smith'
print(data)

new_json = json.dumps(data, indent=4)
print(new_json)
print(type(new_json))
