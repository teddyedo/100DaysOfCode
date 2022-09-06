from art import logo
from deck import *
import random as rd


def pickACard():
    card = rd.choice(deck)
    deck.remove(card)
    return card


def getHandValue(cards):
    handValue = 0
    for card in cards:
        handValue += cardsValue[card]

    for card in cards:
        if card == "A" and handValue > 21:
            handValue -= 10
    return handValue


def busted(cards):
    if getHandValue(cards) > 21:
        return True
    return False


def startGame():
    myCards.append(pickACard())
    myCards.append(pickACard())

    computerCards.append(pickACard())
    computerCards.append(pickACard())

    print("The game has started!")
    print(f"Here is your cards: {myCards}")
    print(f"Here is computer cards: [?, {computerCards[0]}]")


print(logo)

myCards = []
computerCards = []

startGame()

keepGoing = True

while keepGoing:
    print(f"Your hand value is: {getHandValue(myCards)}")
    choice = input("Do you want to pick another card? (y or n): ")
    if choice == "n":
        keepGoing = False
    else:
        myCards.append(pickACard())
        print(myCards)
        if busted(myCards):
            print(
                f"Your actual value is {getHandValue(myCards)}, you are busted!")
            keepGoing = False
