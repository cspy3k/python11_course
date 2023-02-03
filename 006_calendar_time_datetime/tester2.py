import time

start = time.time()

print(time.asctime())
print(time.gmtime())
print(time.localtime())
print(type(time.localtime()))
print(f'{time.localtime()[3]}:{time.localtime()[4]}')

time.sleep(1)

stop = time.time()
print(stop-start)