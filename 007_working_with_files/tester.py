# 'r' - read
# 'a' - append
# 'w' - write
# 'x' - create
# 'r+' - read and write

# file = open('text_files/lorem.txt', 'r', encoding='UTF8')
# print(file.name)
# print(file.mode)
# print(file.encoding)
# print(file.closed)
# file.close()
# print(file.closed)

# file = open(r'text_files/lorem.txt') r'' - raw text \n or any control symbols are ignored

# ABSOLUTE PATH
# C:\Users\Kasutaja\PycharmProjects\python11_course\007_working_with_files\text_files\lorem.txt

# RELATIVE PATH
# 007_working_with_files/text_files/lorem.txt


# with open(r'text_files/lorem.txt', 'r', encoding='UTF8') as file:
#     print(file.closed)
# print(file.closed)

with open(r'text_files/lorem.txt', 'r', encoding='UTF8') as file:
    data = file.readlines()
print(data)
print(type(data))
print(len(data))
# data = file.read(10)
# print(data)
with open(r'text_files/lorem.txt', 'r', encoding='UTF8') as file:
    data = file.readline()
print(data)
print(type(data))
print(len(data))

# with open(r'text_files/lorem.txt', 'r', encoding='UTF8') as file:
#     chunk = 10
#     data = file.read(chunk)
#     file.seek(0)
#     while len(data):
#         print(data)
#         data = file.read(chunk)

with open(r'text_files/tester123.txt', 'w', encoding='UTF8') as file:
    file.write('Hello planet!\n')
 #   file.seek(0)
    file.write('*****')
    pass



