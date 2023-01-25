a = 'Hello'
b = 'World'

print(a, b)
print(a + ' ' + b, 12345, True, False, None, sep = '')
print()
print('line'
      'feed')
print('line\nfeed')

txt = 'Hello\nWorld'
print(len(txt))
print(txt)
print(a + ' ' + b, 12345, True, False, None, sep='***', end='END\n')
print('New Line')

print('that\'s')
print('My favourite music is \"Psy\"')
print('''That's ''')

print('''line1
    line2
line3''')

salary = 2000
name = 'John'
age = 25
txt2 = '{}\' salary is {}. He is {} years old.'
print(txt2.format(name, salary, age))
txt2 = '{2}\' salary is {1}. He is {0} years old.'
print(txt2.format(name, salary, age))

product = 'computer'
price = 1000
txt3 = 'This {product:} costs ${price:.2f}.'
print(txt3.format(product=product, price=price))

x = 1234.123412312423431
y = 123.12333
print('The value of x is %.4f' % x)

emp_name = 'John'
emp_age = '15'
emp_salary = '1000'

# emp_string = ('Hi, my name is %(name)s! I am %(age) years old. My salary is %(salary).' %{'name': emp_name, 'salary': emp_salary, 'age': emp_age})

print(f'Hi, my name is {emp_name.upper()}. I am {emp_age} years old.')
print(f'')
print(emp_name.encode('utf-8'))
