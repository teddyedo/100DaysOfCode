import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException, \
    NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

WEB_DRIVER = "C:\Development\chromedriver.exe"

service = Service(WEB_DRIVER)
driver = webdriver.Chrome(service=service)

driver.get("https://tinder.com/app/recs")

# Select login in Tinder
login_button = driver.find_element(By.XPATH,
                                   '//*[@id="t1452431810"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()

time.sleep(2)

login_with_facebook_button = driver.find_element(By.XPATH,
                                                 '//*[@id="t-275949266"]/main/div/div[1]/div/div/div[3]/span/div[2]/button/div[2]/div[2]')
login_with_facebook_button.click()

time.sleep(4)

base_window = driver.window_handles[0]
login_window = driver.window_handles[1]

driver.switch_to.window(login_window)

buttons = driver.find_elements(By.TAG_NAME, "button")
for button in buttons:
    if button.get_attribute("title") == "Consenti solo i cookie essenziali":
        button.click()

time.sleep(2)

# login on facebook
email_input = driver.find_element(By.ID, 'email')
email_input.send_keys("******************************")
password_input = driver.find_element(By.ID, "pass")
password_input.send_keys("******************************")
password_input.send_keys(Keys.ENTER)

time.sleep(2)

driver.switch_to.window(base_window)

time.sleep(6)

# Dismiss all the requests

consent_button = driver.find_element(By.XPATH,
                                     '//*[@id="t-275949266"]/main/div/div/div/div[3]/button[1]')
consent_button.click()

time.sleep(2)

no_position_button = driver.find_element(By.XPATH,
                                         '//*[@id="t-275949266"]/main/div/div/div/div[3]/button[2]')
no_position_button.click()

time.sleep(2)

consent_cookie_button = driver.find_element(By.XPATH,
                                            '//*[@id="t1452431810"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
consent_cookie_button.click()

# Dislike everybody

for i in range(100):

    time.sleep(2)

    try:
        dislike_button = driver.find_element(By.XPATH,
                                             '//*[@id="t1452431810"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button/span/span')
        dislike_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
