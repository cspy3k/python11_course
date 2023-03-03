import requests
from bs4 import BeautifulSoup as BS

url = 'https://www.ilmateenistus.ee/ilm/ilmavaatlused/vaatlusandmed/oopaevaandmed/'
full_page = requests.get(url, timeout=3)

soup = BS(full_page.content, 'html.parser')
table = soup.table

a_list = list()
a_row = list()
match = table.find_all('td')
print(table)

i = 0
print(len(match))
for name in match:
    s = str(name)
    if i == 0:
        print(i, name)
        a_row.append(s.replace('<td>', '').replace('</td>', ''))
    else:
        s = s.replace('<td class="number">', '').replace('</td>', '')
        if s == '':
            s = None
        a_row.append(s)
    i += 1
    if i == 12:
        i = 0
        a_list.append(a_row)
        a_row=[]
print(a_row)
print(a_list)
