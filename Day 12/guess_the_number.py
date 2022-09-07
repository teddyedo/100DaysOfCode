from operator import mod
from art import logo
import random as rd

print(logo)
print("Welcome to Guess the number!")
mode = input(
    "You have to guess a random number from 1 to 100. Which mode do you choose? (easy or hard): ")
attempts = 0

if mode == "easy":
    attempts = 7
else:
    attempts = 4

randomNumber = rd.randint(1, 100)

gameOver = False

while attempts > 0 and not gameOver:
    print(f"You have {attempts} attempts left.")
    guess = int(input("What number am I thinking about? "))
    if guess == randomNumber:
        print("Exactly! You won!")
        gameOver = True
    elif guess > randomNumber:
        print("Too high.")
        attempts -= 1
    else:
        print("Too low.")
        attempts -= 1
