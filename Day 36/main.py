import requests
from datetime import date, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_API_KEY = "*******************"
NEWS_API_KEY = "************************"


def send_telegram_message(message):
    bot_token = "*****************************************"
    bot_chat_id = "*********************"
    send_text = "https://api.telegram.org/bot" + bot_token + "/sendMessage?chat_id=" + bot_chat_id + "&parse_mode=Markdown&text=" + message

    response = requests.get(send_text)
    response.raise_for_status()

    return response.json()


def get_news(price_difference):
    parameters = {"apikey": NEWS_API_KEY, "pageSize": 3, "q": COMPANY_NAME,
                  "category": "business", "country": "us"}

    response = requests.get("https://newsapi.org/v2/top-headlines", parameters)
    response.raise_for_status()
    message = f"{STOCK}: {price_difference}%\n\n"
    for article in response.json()["articles"]:
        message += "Headline: " + article["title"] + "\n\n"
        message += "Brief: " + article["description"] + "\n"
        message += article["url"] + "\n\n"

    return message


def get_stock_info():
    parameters = {
        "symbol": STOCK,
        "apikey": STOCK_API_KEY
    }
    response = requests.get(
        "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY",
        parameters)
    response.raise_for_status()

    yesterday_info = response.json()["Time Series (Daily)"][
        str(date.today() - timedelta(1))]
    day_before_info = response.json()["Time Series (Daily)"][
        str(date.today() - timedelta(2))]

    percentage_price_difference = round((float(
        yesterday_info["4. close"]) - float(
        day_before_info["4. close"])) / float(yesterday_info["4. close"]) * 100,
                                        2)

    if not - 5 < percentage_price_difference < 5:
        send_telegram_message(get_news(percentage_price_difference))


get_stock_info()
