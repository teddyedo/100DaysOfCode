from bs4 import BeautifulSoup
import requests
import smtplib

URL_PRODUCT = "https://www.amazon.it/Volante-Corsa-Logitech-Driving-Force/dp/B00YUIM2J0"
TARGET_PRICE = 150
MY_EMAIL = "****************"
PASSWORD = "****************"

header = {
    "Accept-Language": "it-IT,it;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
response = requests.get(URL_PRODUCT, headers=header)

soup = BeautifulSoup(response.text, "html.parser")

price_tag = soup.select(selector="#centerCol .a-price-whole")[0]
price = int(price_tag.getText().strip(","))
product_title = soup.select(selector="#productTitle")[0].getText().strip(" ")

if price <= TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(MY_EMAIL, "****************",
                            msg=f"Amazon price alert!\n\n {product_title}: {URL_PRODUCT}")
