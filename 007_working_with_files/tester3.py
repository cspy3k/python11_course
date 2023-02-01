# 'r' - read
# 'a' - append
# 'w' - write
# 'x' - create
# 'r+' - read and write

import datetime
dt = datetime.date.today()
with open(f'text_files/tester123.txt', 'r+') as file:  # not creating a new file!!!
     data = file.read()
     print(data)
     data = file.write(data.upper())
     data = file.read()
     print(data)
