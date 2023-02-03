import datetime
"""
Под каждым комментарием нужно написать одну функцию/программу
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""

# Write a program that converts given string to datetime object
sample1 = 'Jan 1 2014 2:43PM'
sample2 = '14:20 10/12/22'  # YY/MM/DD
sample3 = 'Tuesday, September 24, 2019'
sample4 = '01.01.1970 - 00:00:01'

dt1 = datetime.datetime.strptime(sample1, '%b %d %Y %I:%M%p')
dt2 = datetime.datetime.strptime(sample2, '%H:%M %y/%m/%d')
dt3 = datetime.datetime.strptime(sample3, '%A, %B %d, %Y')
dt4 = datetime.datetime.strptime(sample4, '%d.%m.%Y - %H:%M:%S')
print(dt1)
print(dt2)
print(dt3)
print(dt4)

# Write a program to print yesterdays, today and tomorrow dates
delta24h = datetime.timedelta(days=1)
today = datetime.datetime.now()
print((today - delta24h).strftime('%d.%m.%Y'))
print(today.strftime('%d.%m.%Y'))
print((today + delta24h).strftime('%d.%m.%Y'))

# Write a program to convert given timestamp to dd.mm.yyyy format
some_day = 1014163200
print(datetime.datetime.fromtimestamp(some_day).strftime('%d.%m.%Y'))

# Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)


def sub_2weeks(tstamp):
    new_date = (datetime.datetime.fromtimestamp(tstamp) - datetime.timedelta(days=14))
    return new_date.timestamp()


print(sub_2weeks(1014163200))
