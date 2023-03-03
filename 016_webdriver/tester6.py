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

xpath_url = '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button/span'

accept = driver.find_element('xpath', xpath_url)
accept.click()

videos = driver.find_elements('class name', '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]/div/ytd-rich-item-renderer[1]/div/ytd-rich-grid-media/div[1]/div[2]/div[1]/h3/a/yt-formatted-string')

vid_list = []
for vid in videos:
    title = vid.find_element('xpath', '//*[@id="video-title"]').text
    print(title)

time.sleep(3)
