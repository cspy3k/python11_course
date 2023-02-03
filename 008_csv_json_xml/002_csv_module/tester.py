import csv
import sys

with open('csv_files/test.csv', 'r', encoding='UTF8') as csvfile:
    pass

x = [1, 2, 3, 4, 5]
y = iter(x)
print(y)
print(type(y))

# for i in y:
#     print(i)

print(sys.getsizeof(x))
print(sys.getsizeof(y))

print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
