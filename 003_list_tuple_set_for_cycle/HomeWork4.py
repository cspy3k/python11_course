# id code check/decode/output data
# id code checking

# check if first digit is valid

# check if date of birth is valid

# check if CRC is correct (output might be made anyway)
# id_code = '0123456789A'
# id_code_my = '37906080401'
id_code = '57906080401'
hosp_list = ('Kuressaare haigla', 'Tartu Ülikooli Naistekliinik', 'Ida-Tallinna keskhaigla',
             'Pelgulinna sünnitusmaja (Tallinn)', 'Keila haigla',
             'Rapla haigla, Loksa haigla, Hiiumaa haigla (Kärdla)',
             'Ida-Viru keskhaigla (Kohtla-Järve, endine Jõhvi)',
             'Maarjamõisa kliinikum (Tartu), Jõgeva haigla', 'Narva haigla', 'Pärnu haigla',
             'Haapsalu haigla', 'Järvamaa haigla (Paide)', 'Rakvere haigla, Tapa haigla',
             'Valga haigla', 'Viljandi haigla', 'Lõuna-Eesti haigla (Võru), Põlva haigla')
hosp_code_list1 = [10, 19, 150, 160, 220, 270, 370, 420, 470, 490, 520, 570, 600, 650, 700]
hosp_code_list2 = [[1, 10], [11, 19], [21, 150], [151, 160], [161, 220], [221, 270], [271, 370], [371, 420],
                   [421, 470], [471, 490], [491, 520], [521, 570], [571, 600], [601, 650], [651, 700]]
century_list = [18, 18, 19, 19, 20, 20, 21, 21]


crc_calc1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
crc_calc2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
crc_sum1 = 0
crc_sum2 = 0
# check if input data is valid (11 digits)
# to check it, use .isdecimal() string methgod
# for maternity hospital decoding it's possible to use shorter list and simple conditions
# only additional checking for >1, !20, <701 needed.


# id_YY_code = id_code[:1]
# id_yy = id_code[1:3]
# id_mm = id_code[3:5]
# id_dd = id_code[5:7]
# id_last = id_code[7:10]
# id_crc = id_code[-1]
# print(id_code)
# print(id_YY_code + id_yy + id_mm + id_dd + id_last + id_crc)
# print(id_YY_code)
# print(id_yy)
# print(id_mm)
# print(id_dd)
# print(id_last)
# print(id_crc)

decode_error = False
id_YY = "00"
id_sex = 'unknown'
x = int (id_code[:1])

if (x == 0) or (x == 9):
    decode_error = True
else:
    if (x % 2) == 0:
        id_sex = 'Female'
    else:
        id_sex = 'Male'
    id_YY = str(century_list[(x - 1)])


print(id_code)
print(id_sex)
print(id_YY)
print(decode_error)


#
#
# while True:
#     user_id = input('Please enter id code: ')
#     try:
#         int(user_id)
#         if len(user_id) != 11:
#             raise Exception
#     except ValueError:
#         print('Code is not numeric')
#         continue
#     except Exception:
#         if len(user_id) > 11:
#             print('Too long')
#         else:
#             print('Too short')
#         continue
#     else:
#         print('Your id code is ', user_id)
#         in_data = ''
#         input('Check another ID code?', )
#         break
