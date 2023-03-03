import requests
from requests.exceptions import HTTPError


# 'https://xkcd.com/353/'


# 200 - success
# 300 - redirect
# 400 - client errors
# 500 - server errors

r = requests.get('https://xkcd.com/353/', timeout=3)
# print(r)    # string
# print(r.content)     # bytestring
# print(r.status_code)
# print(r.ok)
# # print(r.headers)
# print(r.encoding)
# print(r.cookies)
# print(r.headers['server'])


# pic = requests.get('https://imgs.xkcd.com/comics/python.png', timeout=3)
# with open('comic.png', 'rb') as file:
#   file.write('comic.png', 'wb')

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        # a = 1 / 0
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error: {http_err}')
    except ZeroDivisionError:
        print('div by 0')
    else:
        print('ok')
