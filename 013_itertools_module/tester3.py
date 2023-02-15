import os
import time

# print(dir(os))  # lists methods and attributes of library

print(os.getcwd())  # gives C_urrent W_orking D_irectory

# os.chdir('../')

print(os.getcwd())
print(type(os.getcwd()))
open(os.getcwd() + '\sample.txt')



print(os.listdir())

#print(os)

# os.mkdir('../999_hello')

os.makedirs('new1/new2/new3')  # returns error only if given directories already exist
time.sleep(3)

os.rmdir('new1/new2/new3')  # removes directory new3
time.sleep(2)

os.makedirs('new1/new2/new3')  # returns error only if given directories already exist
time.sleep(2)

os.removedirs('new1/new2/new3')  # removes directory new3
time.sleep(2)
