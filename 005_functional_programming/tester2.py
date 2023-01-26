# def tester():
#     a = 10
# #    b = 20
#     c = 30
#     print(a, b, c)
#
# a = 1
# b = 2
# c = 3
#
# print(a, b, c)
# tester()

# def test123(a, b, c = 1):
#     return a * b * c
#
# print(test123(10, 5, 3))
# print(test123(c=4, b=5, a=1))

# def tester(a, b=1, *args, **kwargs):
#     print(a, b)
#     print(args)
#     for arg in args:
#         print(arg)
#     print(kwargs)
#
#
# tester(1, 1, 'hello', 123, True, False, None, 3.14, 'hello again!', name='Roman', age='35')

def say_hello():
    print('Hello ', end='')


def take_name(name):
    say_hello()
    print(name)

take_name('Roman')
take_name('Roman')

def wrapper(f):
    print('Starting work')
    f()
    print('Finishing work')


wrapper(say_hello())

# *args       unlimited number of arguments
# *kwargs     unlimited number of arguments with keywords
import functions
print(functions.double(4))
print(functions.triple(4))

from functions import triple as trpl
print(trpl(10))
