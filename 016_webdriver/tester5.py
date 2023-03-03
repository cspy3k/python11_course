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
driver.get(url)

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

accept = driver.find_element('xpath', xpath_url)
accept.click()

current_window = driver.current_window_handle
driver.switch_to.new_window('https://www.github.com')
driver.get('http://www.github.com')
second_window = driver.current_window_handle

driver.switch_to.window(current_window)
time.sleep(4)
driver.switch_to.window(second_window)

for window in driver.window_handles:
    driver.switch_to.window(window)
    driver.save_screenshot(f'{window}.png')
time.sleep(6)