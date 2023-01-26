courses = ['History', 'Math',
           'Literature', 'Physics', 'Programming', 'Math']

for course in courses:
    if course == 'Math':
        print('Math is the best')
    else:
        print(course.upper())

pairs = [[1, 'one'], [2, 'two'], [3,'three']]
print(pairs)

for pair in pairs:
    print(pair)

for num, word in pairs:
    print(num)
    print(word)

pairs2 = [['Jack','Smith', 22], ['Mary', 'Gold', 25], ['Bob', 'Summers', 35]]

for first, last, age in pairs2:
    print(f'Hello {first} {last}. You are {age} years old.')

for num1 in range(10):
    for num2 in range(10):
        for num3 in range(10):
            for num4 in range(10):
                print(num1, num2, num3, num4)
print(list(range(10)))
