import itertools
letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
numbers2 = [4, 5, 4, 3, 2, 1, 0, 4]
selectors = [True, False, False, True]

res = itertools.compress(letters, selectors)
print(list(res))

res = itertools.compress(numbers2, selectors)
print(list(res))

res2 = filter(lambda x: x > 5, numbers2)
print(list(res2))

# def more_than_two(x):
#     return x > 2
#
# res2 = filter(more_than_two(numbers), numbers)
# print(list(res2))
#
# res2 = filterfalse(more_than_two(numbers), numbers)
# print(list(res2))
#
# res = itertools.dropwhile(lambda x: x > 2, numbers2)
# print(list(res))
#
# res2 = itertools.takewhile(lambda x: x > 2, numbers2)
# print(list(res2))

res3 = itertools.accumulate(numbers2)
print(numbers2)
print(list(res3))

