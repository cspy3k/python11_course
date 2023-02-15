import re

with open('people.txt', 'r', encoding='UTF8') as file:
    people_data = file.read()

phones = []
pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
matches = pattern.finditer(people_data)

for match in matches:
    phones.append(match.start())
    phones.append(match.end())
    phones.append(match.group())

# phones.sort()
print(phones)
