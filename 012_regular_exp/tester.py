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

# pattern = re.compile(r'900.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'[89]00.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'[0-37-9]')
# pattern = re.compile(r'[A-B]')
# pattern = re.compile(r'[^w]all')
# pattern = re.compile(r'[a-f^stw]all')
# pattern = re.compile(r'[aft-]')
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
# pattern = re.compile(r'\d{3,4}')    #
# pattern = re.compile(r'M(r|s|rs)')  # неправильная последовательность!!!
pattern = re.compile(r'M(r|s|rs)\.? [A-Z][a-z]*\b')


matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
#    print(match.end())
#    print(match.group())

# pattern = re.compile(r'end$')
# matches = pattern.finditer(sentence)
#
# for match in matches:
#     print(match)

