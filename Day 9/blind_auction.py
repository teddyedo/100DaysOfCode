import os
from art import logo


def clear(): return os.system('cls')


def addBidder(name, bid):
    bids[name] = bid


def findHigestBidder():
    maxBid = 0
    maxBidder = ""
    for bidder in bids:
        if bids[bidder] > maxBid:
            maxBid = bids[bidder]
            maxBidder = bidder

    print(f"The highest bid was made by {maxBidder} with {maxBid} $")


print(logo)

bids = {}
keepGoing = True

while keepGoing:
    name = input("What's your name? ")
    bid = float(input("What's your bid? "))
    addBidder(name, bid)

    choice = input("Do you want to insert another bidder? (yes or no): ")
    if choice == "no":
        keepGoing = False
    clear()

findHigestBidder()
