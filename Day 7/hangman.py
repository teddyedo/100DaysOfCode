import random as r
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

print(logo)

choosenWord = r.choice(word_list)
lives = 6
display = []

for i in range(len(choosenWord)):
    display += "_"

endOfTheGame = False

while not endOfTheGame:

    print(display)
    print(stages[lives])

    choosenLetter = input("Guess a letter: ").lower()

    if choosenLetter not in choosenWord:
        print(f"{choosenLetter} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            endOfTheGame = True
            print(f"You lose. The word was {choosenWord}")

    elif choosenLetter in display:
        print(f"You already guess the letter {choosenLetter}.")

    else:
        for position in range(len(choosenWord)):
            if choosenWord[position] == choosenLetter:
                display[position] = choosenWord[position]
        if "_" not in display:
            endOfTheGame = True
            print("You won!")
