# 5. Написать регулярное выражение для проверки строки, задача определить состоит ли строка из символов a-z, A-Z, 0-9.
#
import re

sample = 'djkahakhjfkfh89798af8a876f098arr'
pattern = re.compile(r'[^\dA-Za-z]')
matches = pattern.findall(sample)

print(matches)
if matches == []:
    print(True)
else:
    print(False)
