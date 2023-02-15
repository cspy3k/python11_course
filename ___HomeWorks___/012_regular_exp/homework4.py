import re

# 4. Написать программу котороая будет выбирать из файла people.txt:
# 	1) Все имена и фамилии
# 	2) Все адреса

with open('people.txt', 'r', encoding='UTF-8') as file:
    data2 = file.read()

name_pattern = re.compile(r'([A-Za-z]+ [A-Za-z-]+)\n')
address_pattern = re.compile(r'\d{3} [0-9A-Za-z]+ St\., [A-Za-z\' -]+ [A-Z]{2}')
matches1 = name_pattern.findall(data2)
print(len(matches1))
matches2 = address_pattern.findall(data2)
print(len(matches2))

people_pairs = zip(matches1, matches2)

people_dict = {}
cnt = 0
for name, address in people_pairs:
    people_dict[cnt] = {'name': name, 'address': address}
    cnt += 1
print(matches1)
print(matches2)
print(people_dict)

