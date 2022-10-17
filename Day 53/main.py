import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

from rent import Rent

FORM_URL = "**********************"
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/"
DRIVER_PATH = "C:\Development\msedgedriver.exe"
RENT_LOCATION = "San Francisco, CA"
MAX_PRICE = 3000

service = Service(DRIVER_PATH)
driver = webdriver.Edge(service=service)


def get_rent_data():
    driver.get(ZILLOW_URL)

    time.sleep(7)

    search_bar = driver.find_element(By.XPATH,
                                     '/html/body/div[1]/div[5]/div/section/div[1]/div/form/div/div/input')
    driver.execute_script('arguments[0].value = "";', search_bar)
    search_bar.send_keys(RENT_LOCATION)

    time.sleep(2)

    price_button = driver.find_element(By.XPATH,
                                       '//*[@id="price"]/button')
    price_button.click()
    time.sleep(2)

    max_price_bar = driver.find_element(By.XPATH,
                                        '/html/body/div[1]/div[5]/div/section/div[2]/div/div[2]/section/div/div/form/div/fieldset/div/div[2]/div/div/div/input')
    max_price_bar.send_keys(3000)
    time.sleep(2)

    beds_button = driver.find_element(By.XPATH,
                                      '//*[@id="beds"]/button')
    beds_button.click()
    time.sleep(2)

    one_or_more_beds_button = driver.find_element(By.XPATH,
                                                  '/html/body/div[1]/div[5]/div/section/div[2]/div/div[3]/div/div/form/fieldset[1]/div[1]/button[2]')
    one_or_more_beds_button.click()

    done_button = driver.find_element(By.XPATH,
                                      '/html/body/div[1]/div[5]/div/section/div[2]/div/div[3]/div/div/div/button')
    done_button.click()

    time.sleep(3)

    houses = driver.find_element(By.XPATH,
                                 '/html/body/div[1]/div[5]/div/div/div[1]/div[1]/ul').find_elements(
        By.TAG_NAME, "li article")

    rents = []

    for house in houses:
        link = house.find_element(By.CSS_SELECTOR, 'div div a').get_attribute(
            "href")
        address = house.find_element(By.CSS_SELECTOR, 'div div a address').text
        price = house.find_element(By.CSS_SELECTOR, 'div div div span').text[:6]

        rents.append(Rent(address, price, link))

    return rents


def save_rent_data(rents):
    driver.get(FORM_URL)
    time.sleep(2)

    for rent in rents:
        address_input = driver.find_element(By.XPATH,
                                            '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_input.send_keys(rent.address)
        price_input = driver.find_element(By.XPATH,
                                          '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_input.send_keys(rent.price)
        link_input = driver.find_element(By.XPATH,
                                         '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_input.send_keys(rent.link)
        send_button = driver.find_element(By.XPATH,
                                          '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')
        send_button.click()
        send_another_answer_button = driver.find_element(By.XPATH,
                                                         '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        send_another_answer_button.click()
        time.sleep(2)


save_rent_data(get_rent_data())
