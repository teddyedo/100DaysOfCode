# Exception handling is part of day 30 lesson

import pandas as pd

data = pd.read_csv("Day 26/nato_phonetic_alphabet.csv")
decodeDict = {row.letter: row.code for (index, row) in data.iterrows()}


def ask():
    word = input("Insert the word you want to convert: ")
    print([decodeDict[char.upper()] for char in word])


keepGoing = True

while keepGoing:

    try:
        ask()
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        keepGoing = False
