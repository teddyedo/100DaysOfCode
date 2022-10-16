import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

SIMILAR_ACCOUNT = "leomessi"
USERNAME = "allari_edoardo"
PASSWORD = "Gervaso23"


class InstaFollower:

    def __init__(self, driver):
        service = Service(driver)
        self.driver = webdriver.Chrome(service=service)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        accept_cookies_button = self.driver.find_element(By.XPATH,
                                                         '/html/body/div[4]/div/div/button[1]')
        accept_cookies_button.click()

        time.sleep(2)

        username_input = self.driver.find_element(By.XPATH,
                                                  '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_input.send_keys(USERNAME)
        password_input = self.driver.find_element(By.XPATH,
                                                  '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_input.send_keys(PASSWORD)
        password_input.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(10)

        inputs = self.driver.find_elements(By.TAG_NAME, "input")
        for input_tag in inputs:
            if input_tag.get_attribute("aria-label") == "Input di ricerca":
                search_bar = input_tag
                search_bar.send_keys(SIMILAR_ACCOUNT)
                search_bar.send_keys(Keys.ENTER)
                time.sleep(2)

        profile_pics = self.driver.find_elements(By.TAG_NAME, "img")

        for img in profile_pics:
            if img.get_attribute(
                "alt") == f"Immagine del profilo di {SIMILAR_ACCOUNT}":
                img.click()

        time.sleep(3)

        profile_to_follow = 0

        divs = self.driver.find_elements(By.TAG_NAME, "div")
        for div in divs:
            if " profili seguiti" in div.text:
                div.click()
                print(
                    div.find_element(By.TAG_NAME, "span").text)

        modal = self.driver.find_element(By.XPATH,
                                                  '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')

        for i in range (10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(1)

        follow_buttons = [button for button in modal.find_elements(By.TAG_NAME, "button") if button.find_element(By.TAG_NAME, "div").find_element(By.TAG_NAME, "div").text == "Segui"]
        [self.follow(button) for button in follow_buttons]

    def follow(self, button):
        button.click()
        time.sleep(2)
