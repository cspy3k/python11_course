import csv

with open('csv_files/test.csv', 'r', encoding='UTF8') as csvfile:
    # csv_reader = csv.reader(csvfile)
    # column_names = next(csv_reader)
    # for line in csv_reader:
    #     print(line)
    csv_reader = list(csv.reader(csvfile))
with open('csv_files/test_copy.csv', 'w', encoding='utf8') as new_file:
    csv_writer = csv.writer(new_file, delimiter=',', lineterminator='\n', quotechar='#')

    for line in csv_reader:
        csv_writer.writerow(line)

with open('csv_files/test_copy.csv', 'r', encoding='utf8') as new_file:
    csv_reader = csv.reader(new_file, delimiter=',')
    for x in csv_reader:
        print(x)
