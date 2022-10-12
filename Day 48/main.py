from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

WEB_DRIVER = "C:\Development\chromedriver.exe"

service = Service(WEB_DRIVER)
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')

upgrades_ids = [upgrade.get_attribute("id") for upgrade in
                driver.find_elements(By.CSS_SELECTOR, "#store div")][:7]


def buy_upgrade():
    upgrades_prices = [int(upgrade.text.split(" - ")[1].replace(",", "")) for
                       upgrade in
                       driver.find_elements(By.CSS_SELECTOR, value="#store b")
                       if upgrade.text != ""]

    upgrades = [{"id": upgrades_ids[i], "cost": upgrades_prices[i]} for i in
                range(len(upgrades_ids))]

    money = get_current_cookies()
    for upgrade in upgrades[::-1]:
        if upgrade["cost"] < money:
            driver.find_element(By.ID, upgrade["id"]).click()
            return


def get_current_cookies():
    return int(driver.find_element(By.ID, value="money").text.replace(",", ""))


def get_cookie_per_sec():
    return float(driver.find_element(By.ID, "cps").text.split(" : ")[1])


timeout = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() > timeout:
        buy_upgrade()
        timeout = time.time() + 5

    if time.time() > five_min:
        print(get_cookie_per_sec())
        break

driver.quit()
