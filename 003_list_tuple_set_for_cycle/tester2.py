courses = {'History', 'Math', 'Literature', 'Physics', 'Programming', 'Math'}
nums = {1, 5, 6, 8, 3, 4, 2}

# empty_set = set()
# print(empty_set)
# print(type(empty_set))

# print(nums)
# courses.remove('Math')
# print(courses)
#
# nums.remove(1)
# x = nums.pop()
# print(nums)
# print(x)
# print(type(nums))
#
# y = ['One', 'Two', 'Three', 'One', 'Two']
# print(list(set(y)))
# y = [4, 2, 5, 7, 23, 1, -1, -2, -3, -8]
# print(list(set(y)))

courses.add('Art')
print(courses)
courses.update(['Art', 'English'])
print(courses)
# courses.clear()
# print(courses)

set1 = {'Math', 'History', 'Physics', 'Art'}
set2 = {'Math', 'Literature', 'Physics', 'English'}
print(set1.union(set2))
print(set1)
print(set2)
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.difference(set1))

x = (1, 2, 3)
y = (1, 2, 3)
z = (2, 1, 3)
print(x == y)
print(x == z)
x = {1, 2, 3}
y = {1, 2, 3}
z = {2, 1, 3}
print(x == y)
print(x == z)
