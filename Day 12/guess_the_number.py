from art import logo
import random as rd

MODE_EASY_ATTEMPTS = 7
MODE_HARD_ATTEMPTS = 4

print(logo)
print("Welcome to Guess the number!")
mode = input(
    "You have to guess a random number from 1 to 100. Which mode do you choose? (easy or hard): ")
attempts = 0

if mode == "easy":
    attempts = MODE_EASY_ATTEMPTS
else:
    attempts = MODE_HARD_ATTEMPTS

numberToGuess = rd.randint(1, 100)

gameOver = False


def playerWon(numberToGuess, playerGuess):
    if playerGuess == numberToGuess:
        print("Exactly! You won!")
        return True
    elif playerGuess > numberToGuess:
        print("Too high.")
        return False
    else:
        print("Too low.")
        return False


while attempts > 0 and not gameOver:
    print(f"You have {attempts} attempts left.")
    playerGuess = int(input("What number am I thinking about? "))
    if playerWon(numberToGuess, playerGuess):
        gameOver = True
    else:
        attempts -= 1

if attempts == 0 and not gameOver:
    print(f"You lost! The number was {numberToGuess}")
