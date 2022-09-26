from tkinter import *
import pandas as pd
import random as rd

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
WORDS_FILE = "data/french_words.csv"
WORDS_TO_LEARN_FILE = "data/words_to_learn.csv"

try:
    data = pd.read_csv(WORDS_TO_LEARN_FILE)
except FileNotFoundError:
    data = pd.read_csv(WORDS_FILE)

words = data.to_dict(orient="records")
word = {}
wordsToLearn = []


def discardWord():
    wordsToLearn.append(word)
    pickNewWord()


def learnedWord():
    words.remove(word)
    data = pd.DataFrame(wordsToLearn)
    data.to_csv(WORDS_TO_LEARN_FILE, index=False)
    pickNewWord()


def showSolution():
    canvas.itemconfig(canvasImage, image=cardBackImage)
    canvas.itemconfig(wordLabel, text=word["English"])
    canvas.itemconfig(languageLabel, text="English")


def pickNewWord():
    global word, flipTimer
    window.after_cancel(flipTimer)
    word = rd.choice(words)
    canvas.itemconfig(canvasImage, image=cardFrontImage)
    canvas.itemconfig(wordLabel, text=word["French"])
    canvas.itemconfig(languageLabel, text="French")
    flipTimer = window.after(3000, showSolution)


# ---------------------- USER INTERFACE --------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flipTimer = window.after(3000, func=showSolution)

wrongImage = PhotoImage(file="images/wrong.png")
wrongButton = Button(
    image=wrongImage, highlightthickness=0, command=discardWord)

rightImage = PhotoImage(file="images/right.png")
rightButton = Button(image=rightImage, highlightthickness=0,
                     command=learnedWord)

canvas = Canvas(width=800, height=526,
                highlightthickness=0, bg=BACKGROUND_COLOR)
cardFrontImage = PhotoImage(file="images/card_front.png")
cardBackImage = PhotoImage(file="images/card_back.png")
canvasImage = canvas.create_image(400, 263, image=cardFrontImage)

languageLabel = canvas.create_text(400, 150, text="French",
                                   font=LANGUAGE_FONT)

wordLabel = canvas.create_text(400, 263, text="Word",
                               font=WORD_FONT)

canvas.grid(row=0, column=0, columnspan=2)
wrongButton.grid(row=1, column=0)
rightButton.grid(row=1, column=1)

pickNewWord()

window.mainloop()

pd.DataFrame.to_csv(data, index=False)
