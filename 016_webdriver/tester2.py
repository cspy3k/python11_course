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

email.send_keys('hello123@examplee.com')
email.send_keys(Keys.ENTER)


def wait_till_clickable(driver, selector_type, selector_value):
    try:
        element = WebDriverWait(driver, timeout=15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="email-container"]/div[2]/button'))
        )
    except:
        print('ERROR')
#        driver.quit()
        return None
    else:
        return element

time.sleep(5)


cont = wait_till_clickable(driver, By.XPATH, '//*[@id="email-container"]/div[2]/button', 15)
if cont:
    cont.click()


# /html/body/div[1]/div[4]/main/div[2]/text-suggester/div[1]/form/div[1]/div[2]/button
# //*[@id="email-container"]/div[2]/button
