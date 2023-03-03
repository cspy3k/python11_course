import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# path="C:\\Programs\\Python36\\BrowersDriver\\geckodriver.exe"

driver = webdriver.Chrome()

driver.get('http://www.gammatest.net')

# # link = driver.find_element('link text', 'Rohkem infot')
# # link = driver.find_element('css selector', '.main .container')
# link = driver.find_element('partial link text', 'Rohkem')
# link.click()
# time.sleep(3)
# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)
# driver.refresh()
# time.sleep(3)
#
#
# print(link.text)
# time.sleep(5)

# link = driver.find_elements('tag name', 'a')
# for l in link:
#     print(l.get_attribute('href'))
#

