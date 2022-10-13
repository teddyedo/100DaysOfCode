from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

JOBS_URL = "https://www.linkedin.com/jobs/search/?currentJobId=3308464205&f_AL=true&f_JT=F&f_TPR=r2592000&f_WT=2&geoId=103350119&keywords=Python%20Developer&location=Italia&refresh=true&sortBy=R"
WEB_DRIVER = "C:\Development\chromedriver.exe"
USERNAME = "**************"
PASSWORD = "**************"

service = Service(WEB_DRIVER)
driver = webdriver.Chrome(service=service)

driver.get(JOBS_URL)

sign_in_button = driver.find_element(By.XPATH,
                                     '/html/body/div[3]/header/nav/div/a[2]')
sign_in_button.click()

time.sleep(3)

email_input = driver.find_element(By.ID, "username")
email_input.send_keys(USERNAME)
password_input = driver.find_element(By.ID, "password")
password_input.send_keys(PASSWORD)
login_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form'
                                             '/div[3]/button')
login_button.click()

time.sleep(5)

jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
for job in jobs:
    job.click()
    time.sleep(2)
    job_save_button = driver.find_element(By.CLASS_NAME, "jobs-save-button")
    job_save_button.click()
    time.sleep(2)