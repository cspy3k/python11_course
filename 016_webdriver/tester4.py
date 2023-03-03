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

# driver.get('https://www.youtube.com/@visitestoniaofficial/videos')
url = 'https://www.youtube.com/@visitestoniaofficial/videos'

# # width = driver.get_window_size().get('width')
# # height = driver.get_window_size().get('height')
# #
# # driver.set_window_size(800, 600)
# #
# # position = driver.get_window_position()
# # print(position)
# # time.sleep(2)
# #
# # driver.set_window_position(100,100)
# # time.sleep(2)
# driver.get(url)
#
# driver.set_window_rect(50,50,800,600)
# time.sleep(2)
#
# driver.fullscreen_window()
# time.sleep(2)
#
# driver.maximize_window()
# time.sleep(2)
#
# driver.minimize_window()
# time.sleep(2)
#
# driver.get(url)
xpath_url = '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/span'

accept = driver.find_element('xpath', '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/span')
accept.click()

driver.save_screenshot('youtube.png')

time.sleep(4)