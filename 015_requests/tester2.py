import requests
from bs4 import BeautifulSoup as BS


url = 'https://gammatest.net/course/python/'
full_page = requests.get(url, timeout=3)
print(full_page.text)
# print(full_page.content)

# soup = BS(full_page.content, 'html.parser')
# print(soup)
# print(soup.title)
# print(soup.table)
# print(soup.prettify)
# print(soup.div.a['href'])
# print(soup.a['href'])
# print(soup.title.parent)
# print(soup.a.parent)

# match = soup.find('div', class_= 'navbar-header')
# print(match.a)
# print(match.a.text)

# match = soup.find(class_= 'navbar-header')
# print(match)
# print(match.a)
# print(match.a.text)

# match = soup.find(href= '/index.php')
# print(match)
# print(match.a)

# match = soup.find_all('div', class_='col-md-4 col-sm-12')
#
# print(type(match))
# print(len(match))
# for div in match:
#     links = div.find_all('a')
#     for link in links:
#         print(link['href'])

# print(soup.contents[3])
