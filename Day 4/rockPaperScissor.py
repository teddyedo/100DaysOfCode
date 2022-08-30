import random as r

possibleChoices = ["R", "P", "S"]

myChoice = int(
    input("What do you choose? (0 for Rock, 1 for Paper and 2 for Scissor): "))
computerChoice = r.randint(0, 2)

if myChoice == computerChoice:
    print("It's a draw")
elif (myChoice + 1) % 3 == computerChoice:
    print("You lost!")
else:
    print("You won!")
