import re

# Sample string
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
Mr.... T
Mr R0123
abc
: ; < = > ? @ _
mall hall wall tall ball call fall
'''

sentence = '\nStart a sentence and then bring it to an end'

# pattern = re.compile(r'\d\d\d')

# matches = pattern.findall(text_to_search)   # creates list
# print(re.findall(r'\d\d\d', text_to_search))

# pattern = re.compile(r'\nABC')
# pattern = re.compile(r'\nabc')

# matches = pattern.match(text_to_search)
# matches = pattern.match(text_to_search)
# findall
# split
# search
# matches = pattern.subn('*', text_to_search, 3)

# pattern = re.compile(r'a', re.IGNORECASE)
# pattern = re.compile(r'^a', re.MULTILINE)
# pattern = re.compile(r'.', re.DOTALL)
pattern = re.compile(r'.#tralala', re.VERBOSE)

matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)


# print(matches)
