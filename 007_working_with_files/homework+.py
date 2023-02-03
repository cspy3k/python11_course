import datetime


start_time = datetime.datetime.now()
print(f'Started:\n', start_time)

with open('text_files/trimushketera.txt', 'r') as file:
    data = file.read().lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '').\
        replace(':', '').replace(';', '').replace('"', '').replace('- ', '').replace('(', '').replace(')', '').\
        replace('*', '').replace('0', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').\
        replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '').replace('0', '')
    words = data.replace('--', '').replace(' -', '').replace('- ', '').split()
#    print(words)
    unique = list(set(words))
    unique.sort()

with open('text_files/new1.txt', 'w', encoding='UTF8') as file:
    file.write(f'The text contains {len(words)} words.\n')
    file.write(f'There are {len(unique)} unique words.\n')
    for word in unique:
        file.write(word + ' \n')

finish_time = datetime.datetime.now()
print(f'Searching for unique words took:\n', (finish_time - start_time))

with open('text_files/new2.txt', 'w', encoding='UTF8') as file:
    file.write(f'The text contains {len(words)} words.\n')
    file.write(f'There are {len(unique)} unique words.\n')
    for word in unique:
        file.write(word + f'  {words.count(word)} \n')

print(f'frequency of words occurrence counting took:\n', (datetime.datetime.now()-finish_time))
print(f'Finished:\n', datetime.datetime.now())
