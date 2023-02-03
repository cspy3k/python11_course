from id_fuctions import *
# idcode = '0123456789A'
# idcode = '37906080401'
# idcode = '57906080401'
# idcode = '38803160272'
# global idcode
idcode = '37906080401'

print('\n\n\n\n\n\n\n')

while True:
    selection = id_menu(idcode)
    if selection == '1':
        idcode_new = id_input()
#        print('\n\n\n\n\n\n\n')
        if not idcode_new:
            continue
        idcode = idcode_new
        print('\n\n\n')
        continue
    if selection == '2':
        print(f'\n\n\n{decode_gender(idcode)}, born in {decode_date(idcode)}'
              f' ({check_date(decode_date(idcode))} date). Place of birth is [{decode_place(idcode)}]')
        print(f'ID number is {check_id(idcode)} !\n')
        continue
    if selection == '3':
        print(f'\n\n\nGender is {decode_gender(idcode)}!\n')
        continue
    if selection == '4':
        print(f'\n\n\nDate of birth is {decode_date(idcode)}, the date is {check_date(decode_date(idcode))}\n')
        continue
    if selection == '5':
        print(f'\n\n\nPlace of birth is [{decode_place(idcode)}]\n')
        continue
    if selection == '6':
        print(f'\n\n\nID number is {check_id(idcode)}!\n')
        continue
    if not selection:
        quit()
    else:
        print('\n\n\n')
        continue
