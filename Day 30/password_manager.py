from tkinter import *
from tkinter import messagebox
import random as rd
import json


LABEL_FONT = ("Arial", 12, "normal")
PASSWORD_FILE = ("Day 30/data.json")

# ---------------- SEARCH PASSWORD ----------------------------- #


def searchCredentials():
    website = websiteEntry.get()

    try:
        with open(PASSWORD_FILE, "r") as passwordFile:
            passwords = json.load(passwordFile)
            credentials = passwords[website]
    except FileNotFoundError:
        messagebox.showwarning("Attention!", message="No password file found")
    except KeyError:
        messagebox.showwarning(
            "Credentials not found", message=f"No credentials founded for website {website}")
    else:
        messagebox.showinfo(
            title="Credentials", message=f"Username: {credentials['username']}\nPassword: {credentials['password']}")
# ---------------- PASSWORD GENERATOR -------------------------- #


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generatePassword():

    passwordEntry.delete(0, END)

    allChars = [rd.choice(letters) for _ in range(8)] + \
        [rd.choice(numbers) for _ in range(4)] + [rd.choice(symbols)
                                                  for _ in range(2)]

    rd.shuffle(allChars)

    passwordEntry.insert(0, "".join(allChars))

# ---------------- SAVE PASSWORD -------------------------- #


def savePassword():
    website = websiteEntry.get()
    username = usernameEntry.get()
    password = passwordEntry.get()
    newData = {website: {
        "username": username,
        "password": password
    }}

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Error", message="You forgot to insert something...")
    else:
        isOk = messagebox.askokcancel(
            title=website, message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \n Do you want to save them?")

        if isOk:
            try:
                with open(PASSWORD_FILE, "r") as passwordFile:
                    passwords = json.load(passwordFile)
            except FileNotFoundError:
                with open(PASSWORD_FILE, "w") as passwordFile:
                    json.dump(newData, passwordFile, indent=4)
            else:
                passwords.update(newData)
                with open(PASSWORD_FILE, "w") as passwordFile:
                    json.dump(passwords, passwordFile, indent=4)

        websiteEntry.delete(0, END)
        passwordEntry.delete(0, END)


# ---------------- UI DESIGN -------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="Day 29/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

websiteLabel = Label(text="Website:", font=LABEL_FONT)
websiteLabel.grid(row=1, column=0)

searchButton = Button(
    text="Search", command=searchCredentials, width=14)
searchButton.grid(row=1, column=2)

usernameLabel = Label(text="Email/Username:", font=LABEL_FONT)
usernameLabel.grid(row=2, column=0)

passwordLabel = Label(text="Password:", font=LABEL_FONT)
passwordLabel.grid(row=3, column=0)

websiteEntry = Entry()
websiteEntry.focus()
websiteEntry.config(width=32)
websiteEntry.grid(row=1, column=1, columnspan=1)

usernameEntry = Entry()
usernameEntry.config(width=50)
usernameEntry.insert(0, "edoardo@email.com")
usernameEntry.grid(row=2, column=1, columnspan=2)

passwordEntry = Entry()
passwordEntry.config(width=32)
passwordEntry.grid(row=3, column=1)

generatePasswordButton = Button(
    text="Generate password", command=generatePassword)
generatePasswordButton.grid(row=3, column=2)

addButton = Button(text="Add", width=42, command=savePassword)
addButton.grid(row=4, column=1, columnspan=2)


window.mainloop()
