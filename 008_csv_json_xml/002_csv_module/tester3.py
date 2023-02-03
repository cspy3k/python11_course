import csv

with open('csv_files/test.csv', 'r', encoding='UTF8') as file:
#    csv_reader = csv.DictReader(file, fieldnames=("name", "date", 'town'))   # not used if csv doesn't have a row names line!
    csv_reader = csv.DictReader(file)  # not used if csv doesn't have a row names line!
#    print(next(csv_reader))
#    for line in csv_reader:
#       print(line)
    with open('csv_files/test_copy2.csv', 'w', encoding='utf8') as file:
        csv_writer = csv.DictWriter(file, lineterminator='\n', delimiter=',', fieldnames=['Name', 'Date of birth', 'Town'])

        # csv_writer.writeheader()
        # for line in csv_reader:
        #     csv_writer.writerow(line)

        csv_writer.writeheader()
        for line in csv_reader:
            for i in line:
                line[i] = line[i].upper()
                print(line)
            csv_writer.writerow(line)
