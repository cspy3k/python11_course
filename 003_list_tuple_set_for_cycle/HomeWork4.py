# id code check/decode/output data



# id code checking
# check if input data is valid (11 digits)
# check if first digit is valid

# check if date of birth is valid

# check if CRC is correct (output might be made anyway)

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
        in_data = ''
        input('Check another ID code?' in_data)
        break

