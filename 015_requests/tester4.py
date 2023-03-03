import requests
from bs4 import BeautifulSoup as BS
import re

eur_to_yen = 'https://www.google.com/search?q=eur+to+yen&newwindow=1&client=firefox-b-d&ei=W3fuY4uMJ86GrwSJmIPgAw&ved=0ahUKEwjLpYim15r9AhVOw4sKHQnMADwQ4dUDCA4&uact=5&oq=eur+to+yen&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIKCAAQkQIQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIJCAAQFhAeEPEEMgkIABAWEB4Q8QQyCQgAEBYQHhDxBDoKCAAQRxDWBBCwAzoHCAAQsAMQQzoECAAQQzoHCAAQgAQQCjoFCAAQkQJKBAhBGABQiwhY3hdgjiloAXABeACAAcYBiAG6BJIBAzUuMZgBAKABAcgBCsABAQ&sclient=gws-wiz-serp'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
full_page = requests.get(eur_to_yen, timeout=3, headers=headers)
soup = BS(full_page.content, 'html.parser')

rate = soup.find('span', class_='DFlfde SwHCTb')
rate = float(rate['data-value'])

user_amount = float(input('Please enter amount in EUR: '))
print(user_amount * rate)

user_amount = float(input('Please enter amount in YEN: '))
print(user_amount / rate)
