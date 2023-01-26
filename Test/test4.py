data_list = list()

while True:
    xxx = input('Enter any data step by step, \"<ENTER>\" to stop input: ')

    if xxx == "" or xxx == "\x0d":
        break
    else:
        data_list.append(xxx)
        continue
print("data_list: ")
print(data_list)

for xxx in data_list:
    print(xxx)
