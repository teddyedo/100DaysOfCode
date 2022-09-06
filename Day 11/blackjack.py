from art import logo
from deck import *
import random as rd


def pickACard():
    card = rd.choice(deck)
    deck.remove(card)
    return card


def calculateHandValue(cards):
    handValue = 0
    for card in cards:
        handValue += cardsValue[card]

    for card in cards:
        if card == "A" and handValue > 21:
            handValue -= 10
    return handValue


def busted(cards):
    if calculateHandValue(cards) > 21:
        return True
    return False


def startGame():
    for i in range(2):
        myCards.append(pickACard())
        computerCards.append(pickACard())

    print("The game has started!")
    print(f"Here is your cards: {myCards}")
    print(f"Here is computer cards: [?, {computerCards[0]}]")


print(logo)


myCards = []
computerCards = []

startGame()

takeAnotherCard = True

while takeAnotherCard:
    print(f"Your hand value is: {calculateHandValue(myCards)}")
    choice = input("Do you want to pick another card? (y or n): ")
    if choice == "n":
        takeAnotherCard = False
    else:
        myCards.append(pickACard())
        print(myCards)
        if busted(myCards):
            print(
                f"Your actual value is {calculateHandValue(myCards)}, you are busted!")
            takeAnotherCard = False

computerTurn = True

print(f"These are the computer cards: {computerCards}")

while computerTurn:
    if calculateHandValue(computerCards) > calculateHandValue(myCards):
        if not busted(computerCards):
            print("Computer won!")
        else:
            print("Computer busted. You won!")
        computerTurn = False
    elif calculateHandValue(computerCards) == calculateHandValue(myCards):
        print("It's a draw!")
        computerTurn = False
    else:
        computerCards.append(pickACard())
        print(
            f"Computer pick another card. These are the computer cards: {computerCards}")
