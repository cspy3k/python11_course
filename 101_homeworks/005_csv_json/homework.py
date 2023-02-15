import csv

with open('data/happiness.csv', 'r', encoding='UTF-8') as file:
    happiness_data = list(csv.reader(file))

analysis_data = []
for line in happiness_data:
    analysis_data.append([line[3],line[1]])

print(analysis_data)

# x=[[1,5], [5,2], [3,4], []]

analysis_data.sort(reverse=True)

result = []
for line in analysis_data:
    if analysis_data.index(line) > 9:
        break
    result.append(line)

for line in result:
    print(line[1], line[0])
