# Для диапазона чисел от 0 до 100 включительно.
# Если число делится на 3 без остатка - написать число и Fizz
# Если число делится на 5 без остатка - написать число и Buzz
# Если число делится на 3 и на 5 без остатка - написать число и FizzBuzz

result_lst = [0, 0, 0]

for num in range(0, 101):
    if (num % 3 == 0) and (num % 5 == 0):
        print(f'{num} FizzBuzz')
        result_lst[0] += 1
    elif num % 3 == 0:
        print(f'{num} Fizz')
        result_lst[1] += 1
    elif num % 5 == 0:
        print(f'{num} Buzz')
        result_lst[2] += 1
print(f'Fizzbuzz:{result_lst[0]} Fizz:{result_lst[1]} Buzz:{result_lst[2]}')
