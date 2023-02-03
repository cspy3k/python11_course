import datetime
import os
from time import sleep


def clear():
    os.system('cls')
    return()


def decode_id(idcode):
    print(decode_gender(idcode))
    print(decode_date(idcode))
    print(decode_place(idcode))
    print(check_id(idcode))
    return


def decode_date(idcode):
    id_yy1_code = idcode[:1]
    id_yy0 = idcode[1:3]
    id_mm = idcode[3:5]
    id_dd = idcode[5:7]
    id_yy1 = ''

    if id_yy1_code == '1' or id_yy1_code == '2':
        id_yy1 = '18'
    if id_yy1_code == '3' or id_yy1_code == '4':
        id_yy1 = '19'
    if id_yy1_code == '5' or id_yy1_code == '6':
        id_yy1 = '20'
    if id_yy1_code == '7' or id_yy1_code == '8':
        id_yy1 = '21'
    if id_yy1_code == '0' or id_yy1_code == '9':
        id_yy1 = 'xx'
    id_date = id_dd + '.' + id_mm + '.' + id_yy1 + id_yy0
    return id_date


def check_date(id_date):
    try:
        datetime.datetime.strptime(id_date, '%d.%m.%Y')
        return 'valid'
    except ValueError:
        return 'invalid'


def is_valid_date(year, month, day):
    day_count_for_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        day_count_for_month[2] = 29
    return 1 <= month <= 12 and 1 <= day <= day_count_for_month[month]


def decode_gender(idcode):
    if int(idcode) == 0 or int(idcode) == 9:
        return 'unknown, code is not valid!!!'
    if int(idcode[0]) % 2:
        return 'Male'
    return 'Female'


def id_input():
    print('\n\n\n\n\n\n\n\n\n\n\n')
    while True:
        clear()
        idcode_in = input('Enter ID code number (Type "exit" or press <enter> to stop): ')
        if idcode_in == '' or idcode_in.lower() == 'exit':
            return False
        if idcode_in.isdecimal():
            if len(idcode_in) == 11:
                return idcode_in
            elif len(idcode_in) > 11:
                print(f'ID number must have 11 digits but entered value has ', len(idcode_in), '! It\'s too long!')
                continue
            elif len(idcode_in) < 11:
                print(f'ID number must have 11 digits but entered value has ', len(idcode_in), '! It\'s too short!')
                continue
        else:
            print('Value is not numeric!')
            continue


def id_menu(idcode):
    print(f'1. Change ID code\n2. Full decode\n3. Show Gender\n4. Show date of birth\n5. Show place of birth\n'
          f'6. Validation check\n')
    print(f'ID={idcode}       Enter number 1...6, type "exit" or press <enter> to stop program: ', end='')
    selection = input()
    if selection.lower() == 'exit':
        selection = ''
    return selection


hosp_list = ['Kuressaare haigla', 'Tartu Ülikooli Naistekliinik',
             'Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja (Tallinn)',
             'Keila haigla', 'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)',
             'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)',
             'Maarjamõisa kliinikum (Tartu), Jõgeva haigla', 'Narva haigla', 'Pärnu haigla',
             'Haapsalu haigla', 'Järvamaa haigla (Paide)', 'Rakvere haigla, Tapa haigla',
             'Valga haigla', 'Viljandi haigla', 'Lõuna-Eesti haigla (Võru), Põlva haigla']
hosp_code = [[1, 10], [11, 19], [21, 150], [151, 160], [161, 220], [221, 270], [271, 370], [371, 420],
             [421, 470], [471, 490], [491, 520], [521, 570], [571, 600], [601, 650], [651, 700]]


def decode_place(idcode):
    value = int(idcode[7:10])
    if (not value) or (value > 700):
        return 'UNDEFINED'

    for n in range(0, 15):
        if hosp_code[n][0] <= value <= hosp_code[n][1]:
            return hosp_list[n]


def check_id(idcode):
    crc_calc1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1)
    crc_calc2 = (3, 4, 5, 6, 7, 8, 9, 1, 2, 3)
    checksum = 0
    count = 0
    for n in crc_calc1:
        checksum += n * int(idcode[count])
        count += 1
    if (checksum % 11) == int(idcode[10]):
        return 'valid'
    elif (checksum % 11) == 10:
        checksum = 0
        count = 0
        for n in crc_calc2:
            checksum += n * int(idcode[count])
            count += 1
        if (checksum % 11) == int(idcode[10]):
            return 'valid'
    return 'not valid'
