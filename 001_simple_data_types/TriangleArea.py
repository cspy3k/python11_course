side_a = float(input('Please enter side A: '))
side_b = float(input('Please enter side B: '))
side_c = float(input('Please enter side C: '))
hp = (side_a + side_b + side_c) / 2
area = (hp * (hp - side_a) * (hp - side_b) * (hp - side_c)) ** 0.5
print('The area of triangle with sides ' + str(side_a) + ', ' + str(side_b) + ', ' + str(side_c) + ' is ' + str(area) + '.')

