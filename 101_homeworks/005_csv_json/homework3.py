def squares(number):
    return number ** 2

def sorting(value):
    return value[1]

x = [[1, 5],[3, 6], [7, 2], [2, 1]]
print(x)
# x.sort()
# print(x)

# x.sort(key=sorting)
# print(x)

x.sort(key=lambda value: value[1])
print(x)

sum_numbers = lambda a, b: a + b
print(sum_numbers(2, 5))
