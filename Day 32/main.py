import smtplib
import pandas as pd
import datetime as dt
import random as rd

MY_EMAIL = "********************"
PASSWORD = "*****************"
BIRTHDAYS_FILE = "birthdays.csv"
LETTER_TEMPLATES = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
NAME_PLACEHOLDER = "[NAME]"


def send_email(receiver, msg):
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(MY_EMAIL, receiver, msg="Subject:Happy Birthday!\n\n" +msg)


data = pd.read_csv(BIRTHDAYS_FILE)
birthdays = []
today = dt.datetime.now()

for index, row in data.iterrows():
    if row.month == today.month and row.day == today.day:
        birthdays.append(row)

for birthday in birthdays:
    template_letter = rd.choice(LETTER_TEMPLATES)
    with open("letter_templates/" + template_letter, "r") as letterFile:
        letter = letterFile.read()
        letter = letter.replace(NAME_PLACEHOLDER, birthday["name"])
    receiver = birthday["email"]
    send_email(receiver, letter)