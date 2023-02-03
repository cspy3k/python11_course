import json


with open('001_json_module/sample2.json', 'r', encoding='UTF8') as file:
    data = json.load(file)

for person in data['people']:
    if person['has_licence'] == False:
        data['people'].remove(person)

with open('001_json_module/sample2_edit.json', 'w', encoding='UTF8') as file:
    json.dump(data, file, indent=2)
