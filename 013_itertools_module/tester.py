# # import itertools
# #
# # counter = itertools.count()
# # print(counter)
# #
# # x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# #
# # for i in x:
# #     print(next(counter), ':', i, sep='')
# #
# import itertools
#
#  counter = itertools.count()
# data = [100, 200, 300, 400]
#
# dayly_data = zip(counter, data)
# print(list(dayly_data))
#
# # print(list(enumerate('100')
#
# daily_data = itertools.zip_longest(data, range(10), fillvalue=False)
# print(list(daily_data))

import itertools

counter = itertools.count(start=-10.5, step=-0.5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

counter = itertools.cycle([1, 2, 3])
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

counter = itertools.cycle(['even', 'odd'])
for x in range(100):
    print(x, next(counter))


counter = itertools.repeat(3)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))


result = map(lambda x, y: x ** y, range(100), itertools.repeat(2))
for x in result:
    print(x)

result = itertools.starmap(lambda x, y: x ** y, [(0, 2), (1, 2), (3, 5)])
for x in result:
    print(x)

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
numbers2 = (0, 1, 2, 3)
names = ['Jack', 'Sarah']


res = itertools.combinations(letters, 4)  # NO ORDER, NO REPEAT
n = 0
for x in res:
    print(x)
    n += 1
print(n)

res = itertools.permutations(letters, 4)  # ORDERED, NO REPEAT
n = 0
for x in res:
    print(x)
    n += 1
print(n)

res = itertools.product(numbers, repeat=4)
n = 0
for x in res:
    print(x)
    n += 1
print(n)

res = itertools.product(numbers, letters, repeat=2)  # ORDERED, REPEATING
n = 0
for x in res:
    print(x)
    n += 1
print(n)

res = itertools.combinations_with_replacement(numbers, 4)  # NO ORDER, REPEATING
n = 0
for x in res:
    print(x)
    n += 1
print(n)
itertools.product()


combined = itertools.chain((letters, numbers))
n = 0
for x in res:
    print(x)
    n += 1
print(n)

combined = itertools.islice({1, 2, 3, 4, 5, 6, 7, 8}, 0, 5, 2)
print(list(combined))

with open(demo_)