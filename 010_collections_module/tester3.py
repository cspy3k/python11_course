# # from collections import OrderedDict
# #
# # ordereddict = OrderedDict()
# # ordereddict['Name'] = 'Jack'
# # ordereddict['Surname'] = 'Smith'
# #
# # print(ordereddict)
#
# from collections import defaultdict
#
# default = defaultdict(int)
# default['a'] = 1
# default['b'] = 2
# print(default['c'])

from collections import deque

d = deque()
#
# d.append(1)
# d.append(2)
# print(d)
# d.appendleft(3)
# print(d)
#
# x = d.popleft()
# print(x)
# print(d)
#
# d.extendleft([7, 8, 9])
# print(d)


d.append(1)
d.append(2)
d.append(3)

print(d)

d.rotate(-2)
print(d)
