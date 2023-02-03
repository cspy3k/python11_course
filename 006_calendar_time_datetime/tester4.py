import datetime

today = datetime.datetime.now()
print(today)
print(today.strftime('%A %d.%m.%y %H:%M\n'))

tdelta = datetime.timedelta(hours=5)
print(datetime.timezone(offset=tdelta))
print()

dt_str = 'November 30, 2020 15:23'
new_date = datetime.datetime.strptime(dt_str, '%B %d, %Y %H:%M')
print(new_date)
print(type(new_date))
print()

print(today.timestamp())
print(datetime.datetime.fromtimestamp(1675285231.557233))
print(datetime.datetime.fromtimestamp(1675285231))


