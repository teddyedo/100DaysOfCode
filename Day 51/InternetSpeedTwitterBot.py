import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

TWITTER_EMAIL = "************************"
TWITTER_PASSWORD = "************************"


class InternetSpeedTwitterBot:

    def __init__(self, driver):
        service = Service(driver)
        self.driver = webdriver.Chrome(service=service)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        accept_cookie_button = self.driver.find_element(By.XPATH,
                                                        '//*[@id="onetrust-accept-btn-handler"]')
        accept_cookie_button.click()
        time.sleep(1)

        start_test_button = self.driver.find_element(By.XPATH,
                                                     '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start_test_button.click()
        time.sleep(60)
        self.down = float(self.driver.find_element(By.XPATH,
                                                   '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH,
                                                 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        print(self.down)
        print(self.up)

    def tweet_to_provider(self, prom_up, prom_down):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(2)

        # Login
        email_input = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email_input.send_keys(TWITTER_EMAIL)
        email_input.send_keys(Keys.ENTER)
        time.sleep(2)

        password_input = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(TWITTER_PASSWORD)
        password_input.send_keys(Keys.ENTER)
        time.sleep(2)

        # Tweet
        tweet_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        tweet_button.click()
        time.sleep(2)

        tweet_box = self.driver.find_element(By.XPATH,
                                             '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_box.send_keys(
            f"Hey Internet provider, why is my internet speed {self.down} down / {self.up} up when I pay for {prom_down}/{prom_up}?")
        publish_button = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span')
        publish_button.click()
