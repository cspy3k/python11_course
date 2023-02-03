with open(r'text_files/trimushketera.txt', 'r', encoding='UTF8') as input_file:
    in_data = input_file.read().lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace(
        ':', '').replace(';', '').replace('"', '').replace('- ', '').replace('\n',' ')
#    in_data.replace('  ',' ')
#    for char in ['!', '?']:
#        in_data.replace(char, '')
    a = in_data.split()
    print(a)
#    chars_remove = ',.:;!?"'
#    in_data = input_file.read().translate(str.maketrans('', '', chars_remove))
with open(r'text_files/new.txt', 'w', encoding='UTF8') as output_file:
    output_file.write(in_data)
#dict1 = []
#for word in a