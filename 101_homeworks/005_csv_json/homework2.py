import csv

with open('data/happiness.csv', 'r', encoding='UTF8') as file:
    happiness_data = csv.DictReader(file)
    next(happiness_data)
    happiness_data = list(happiness_data)
# print(happiness_data)
# happiness_data.sort(reverse=True, key=lambda happiness_data:[5])
# print(happiness_data)


analysis_data = []
for line in happiness_data:
    analysis_data.append([line['Social support'], line['Country or region']])

analysis_data.sort(reverse=True)

result = []
for line in analysis_data:
    if analysis_data.index(line) > 9:
        break
    result.append(line)

for line in result:
    print(line[1], line[0])
