from InstaFollower import InstaFollower

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

instaFollower = InstaFollower(CHROME_DRIVER_PATH)

instaFollower.login()
instaFollower.find_followers()