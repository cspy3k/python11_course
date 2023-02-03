# for x in range(10):
#     if x == 5:
#         continue
#     if x == 8:
#         break
#     print(x)
#
# count = 0
# while True:
#     print(count)
#     if count == 100:
#         break
#     count += 1

# while True:
#     try:
#         user_input = float(input('Enter number: '))
#     except:
#         print('wrong data!')
#     else:
#         print(user_input ** 2)
#         break
# print('good bye!')

while True:
    user_id = input('Please enter id code: ')
    try:
        int(user_id)
        if  len(user_id) != 11:
            raise Exception
    except ValueError:
        print('Code is not numeric')
        continue
    except Exception:
        if  len(user_id) > 11:
            print('Too long')
        else:
            print('Too short')
        continue
    else:
        print('Your id code is ', user_id)
        break
