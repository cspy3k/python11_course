import re
# 6. Написать регулярное выражение для определения эстонского личного кода (isikukood)
#
# Все строки произвольные.
sample = '37906010401 37906010401 3790601040137906410401 37906010401 97926510401 3790601040137906010401'
pattern = re.compile(r'[1-8][0-9]{2}(0[1-9]|1[0-2])(0[1-9]|[12])\d{4}')

matches = pattern.findall(sample)
print(len(matches))
matches = pattern.finditer(sample)
for m in matches:
     print(m)
