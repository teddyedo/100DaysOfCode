print("Welcome to Treasure Island!")
print("Your mission is to find the treasure. Answer correctly and you will find the treasure!")

carChoice = input(
    "In front of you there are two cars, one on the left, one on the right. Which one you choose? (L or R): ")

if carChoice == "L":
    print("Game over! You choose the wrong car!")
else:
    fightOrRunChoice = input(
        "In the distance you see a bunch of zombies. You fight them or you run away? (Fight or Run): ")
    if fightOrRunChoice == "Run":
        print("Game over! What a coward you are!")
    else:
        doorChoice = input(
            "Now you are standing in front of two doors, one blue, one red. Where is the treasure? (Blue or Red): ")
        if doorChoice == "Blue":
            print("Game over! You were so close!")
        else:
            print("Yeah! You found the treasure!")
