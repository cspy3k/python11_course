import datetime

d = datetime.datetime.today()
dd = datetime.datetime.now()
print(d)
print(dd)

# print(today)
# print(type(today-d))
#
# print(today.weekday())
# print(today.isoweekday())

# today = datetime.date.today()
# tdelta = datetime.timedelta(hours=12)
# d += tdelta
# print(d)

# today = datetime.date.today()
# tdelta = datetime.timedelta(days=365, minutes=12, hours=3)
# print(tdelta)
# d += tdelta
# print(d)
# print(tdelta.total_seconds())
#

t = datetime.time(14, 25, 10, 4534)
print(t)
print(type(t))
tdelta = datetime.timedelta(days=365)
print(tdelta)

print(d + tdelta)
print(d - tdelta)
