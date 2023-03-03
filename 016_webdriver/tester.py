from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# path="C:\\Programs\\Python36\\BrowersDriver\\geckodriver.exe"

driver = webdriver.Chrome()

driver.get('http://www.github.com')

# print(driver.title)
email = driver.find_element('id', 'user_email')

email.send_keys('hello@example.com')
email.send_keys(Keys.ENTER)

try:
    element = WebDriverWait(driver, timeout=15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="email-container"]/div[2]/button'))
    )
    element.click()
except:
    print('ERROR')
    driver.quit()

cont = driver.find_element('xpath', '//*[@id="email-container"]/div[2]/button')
time.sleep(9)
cont.click()
time.sleep(5)

# /html/body/div[1]/div[4]/main/div[2]/text-suggester/div[1]/form/div[1]/div[2]/button
# //*[@id="email-container"]/div[2]/button
