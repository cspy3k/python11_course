seconds = input('Enter seconds: ')
seconds = int(seconds)
dd = seconds % (24*60*60)
seconds = seconds // (24*60*60)
hh = seconds % (3600)
seconds = seconds // (3600)
mm = seconds % 60
seconds = seconds // 60

print (dd + ":" + hh + ":" + mm + ":" + seconds)


