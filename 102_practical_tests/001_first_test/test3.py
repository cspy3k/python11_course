a, b, c = input('enter triangle 3 side lengths: ').split()
a, b, c = float(a), float(b), float(c)
x = c ** 2
y = a ** 2 + b ** 2
if x == y:
    print('This triange is rectangular!')
else:
    print('This is not a rectangular triangle!')
