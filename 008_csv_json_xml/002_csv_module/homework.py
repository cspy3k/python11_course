# выписать топ 10 по любому из параметров
# реализовать через меню - выдавать несколько столбцов вместе с выбранным для сортировки?
# file = 2019.csv

import csv
with open('csv_files/2019.csv', 'r', encoding='UTF8') as read_file:
    csv_reader = list(csv.DictReader(read_file))
    print(csv_reader)

