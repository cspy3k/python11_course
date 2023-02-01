# 'r' - read
# 'a' - append
# 'w' - write
# 'x' - create
# 'r+' - read and write

import datetime
dt = datetime.date.today()
# with open(f'text_files/{dt}.txt', 'w', encoding='UTF-8') as file:
#     file.write('Hello World!')
#     pass
with open(r'text_files/lorem.txt', 'r', encoding='UTF8') as read_file:
    data = read_file.read()
with open(r'text_files/tester.txt', 'w', encoding='UTF8') as file:
    file.write(data.upper())
