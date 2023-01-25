string_sample1 = 'Hello world WORLD'
string_sample2 = 'first letteR is lowErcase. and now?'
string_sample3 = '* * * * * * * extra whitespaces     *'
german_sample = 'der Fluß'

# [START:END:STEP]
print(string_sample1[1])  # output = 'e' as in Python string literal index starts from 0
print(string_sample1[-1])  # output = 'd' last character in string, negative indexes are counted backward
print(string_sample1[:5])  # output = 'Hello'
print(string_sample1[::2])
print(string_sample1[::-1])

print(len(string_sample1))  # String length (int)
print(string_sample1[len(string_sample1)-1])
print(string_sample1.upper())

print(german_sample.casefold())

print(len(german_sample.lower()))
print(len(german_sample.casefold()))

print(string_sample1.isupper())  # check if all string's characters are in upper case
print(string_sample1.islower())

print(string_sample2.capitalize())  # converts first character of first word in string into upper case
#                                     and others into lower case
print(string_sample2.title())  # converts first characters of every word in string into upper case

print(string_sample3.strip())
print(string_sample3.strip('*'))

print(string_sample3.rstrip('* '))
print(string_sample3.lstrip('* '))

print(string_sample1.replace('world','planet',1))
print(string_sample3.replace('*','$'))

print(string_sample1.split())

a, b, c = (string_sample1.split())
print(a)
print(b)
print(c)

#a, b, c = input('Please enter 3 numbers: ').split()


print(string_sample1.count("world"))
print(string_sample1.find("world"))  # gives index of searched string

print('world' in string_sample1)
