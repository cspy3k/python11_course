import requests
from bs4 import BeautifulSoup as BS
import re

url = 'https://gammatest.net/course/python/'
full_page = requests.get(url, timeout=3)

soup = BS(full_page.content, 'html.parser')

# print(soup.find(string=re.compile(r'^Пе')))
# print(soup.find_all(['a', 'table']))

# for tag in soup.find_all(True):         # похоже на os.walk(), перебирает все теги и вложения рекурсивно
#     print(tag)

# for tag in soup.find_all('a', string='Перейти', limit=10):
#     print(tag)

# test_link = soup.find('a', string='Eesti keeles')
# print(test_link.find_parents(['div']))

test_link = soup.find('a', string='Eesti keeles')
# print(test_link.find_parent().find_parent())
print(test_link.find_previous_sibling().find_next_sibling())
print(soup.find('div', class_='col-md-4').find_next_siblings(class_="col-md-8"))
print(test_link.find_next()) # next element (.find_previous, find_allnext, find_allprevious
