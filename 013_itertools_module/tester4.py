import os
import time
import sys


# #
# # os.rename('sample.txt', 'test.txt')
# # os.rename('test.txt', 'sample.txt')
# #
# # os.mkdir('new')
# # os.rename('sample.txt', 'sample.txt')
#
# # os.remove('sample.txt')   # remove file
#
# print(os.stat('sample.txt'))
# print(os.stat('sample.txt').st_size)
#
# info = os.walk('../')
#
# for dirpath, dirnames, filenames in info:
#     if '.git' in dirpath:
#         pass
#     else:
#         print('Current DIR: ' + dirpath)
#         print('Directories: ' + str(dirnames))
#         print('Files: ' + str(filenames))
#         if 'tester.py' in filenames:
#             print('*' * 20)
#             print(dirpath)
#             print('*' * 20)
#         print()

print(os.getpid())
filepath = os.path.join('C:\\Home\SomeDir', 'sample.txt')
print(filepath)

print(os.path.basename(filepath))
print(os.path.dirname(filepath))
print(os.path.split(filepath))
print(os.path.splitext(filepath))

print(os.path.exists('../001_simple_data_types'))

print(os.path.isdir('../001_simple_data_types'))
print(os.path.isdir('../001_simple_data_types/cheat_sheets/002_python_assignment_operators.png'))

print(os.path.isfile('../001_simple_data_types/cheat_sheets/002_python_assignment_operators.png'))

print(sys.getsizeof(filepath))

