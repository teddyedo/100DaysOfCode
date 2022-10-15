from InternetSpeedTwitterBot import InternetSpeedTwitterBot

PROMISED_DOWN = 200
PROMISED_UP = 100

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

internetSpeedTweetBot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

internetSpeedTweetBot.get_internet_speed()

if PROMISED_UP > internetSpeedTweetBot.up or PROMISED_DOWN > internetSpeedTweetBot.down:
    internetSpeedTweetBot.tweet_to_provider(PROMISED_UP, PROMISED_DOWN)