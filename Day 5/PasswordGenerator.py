import random as rd

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")
numberOfLetters = int(input("How many letters do you want in your password? "))
numberOfNumbers = int(input("How many numbers do you want in your password? "))
numberOfSymbols = int(
    input("How many special characters do you want in your password? "))

allChars = []

for char in range(1, numberOfLetters + 1):
    allChars.append(rd.choice(letters))

for char in range(1, numberOfNumbers + 1):
    allChars.append(rd.choice(numbers))

for char in range(1, numberOfSymbols + 1):
    allChars.append(rd.choice(symbols))

rd.shuffle(allChars)

password = "".join(allChars)

print(f"Your new password is: {password}")
