import re

# 2. Создать запрос для определения в тексте цифр, за которыми не стоит знак +. (Примеры выражений “2*9-6*5” или (3+5)-9*4)
# самому решить не получилось(

sample = "213+34*232+23-232+323 32+323"
# pattern = re.compile(r'\d+(^+\d]|\d+$)', re.IGNORECASE)
pattern = re.compile(r'(\d+)[^+\d]|(\d+$)')
matches = pattern.finditer(sample)

# for match in matches:
#     print(match)
for match in matches:
    print(match.group(1) or match.group(2))
