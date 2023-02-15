import re
with open('text_files/trimushketera.txt', 'r', encoding='UTF8') as file:
    data = file.read()

# words = re.sub(r'[^A-Za-zА-Яа-я\'\s-]', '', data).lower().split()
# pattern = re.(r'[^A-Za-zА-Яа-я\'\s-]', '', d
#
# words = pattern.sub('', data).lower().split()
#
# unique = list(set(words))
# unique.sort()


pattern = re.compile(r'[^A-Za-zА-я\'\s-]')
words = pattern.sub('', data).lower().split()
unique = list(set(words))
unique.sort()




with open('text_files/trimushketera_out.txt', 'w', encoding='UTF8') as file:
    file.write(f'There are {len(words)} words.\n')
    file.write(f'There are {len(unique)} unique words.\n')
    for word in unique:
        file.write(word + f'{word}\n')




with open('text_files/trimushketera_copy.txt', 'w', encoding='UTF8') as file:
    file.write(f'There are {len(words)} words.\n')
    file.write(f'There are {len(unique)} unique words.\n')
    for word in unique:
        file.write(word + f'{word}\n')
