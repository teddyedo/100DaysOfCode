import pandas as pd

data = pd.read_csv("Day 26/nato_phonetic_alphabet.csv")
decodeDict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Insert the word you want to convert: ")

print([decodeDict[char.upper()] for char in word])
