from data import MENU
from data import resources


def chooseDrink():
    return input("What would you like? (espresso/latte/cappuccino): ")


def turnOff():
    print("Coffee machine is in manteinance mode.")


def showReport():
    print("Coffee machine resources:")
    print(f"Water: {resources['water']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Milk: {resources['milk']} ml")
    print(f"Money: ${resources['money']}")


def resourcesAreEnough(drink):
    drinkRecipe = MENU[drink]
    if drinkRecipe["ingredients"]["water"] > resources["water"]:
        print("Sorry, there isn't enough water")
        return False
    if drinkRecipe["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry, there isn't enough coffee")
        return False
    if drink == "latte" or drink == "cappuccino":
        if drinkRecipe["ingredients"]["milk"] > resources["milk"]:
            print("Sorry, there isn't enough milk")
            return False
    return True


def getTheCoins(drink):
    print("Time to insert some money: ")
    pennies = int(input("Insert pennies: "))
    nickles = int(input("Insert nickles: "))
    dimes = int(input("Insert dimes: "))
    quarters = int(input("Insert quarters: "))

    return round((pennies + nickles * 5 + dimes * 10 + quarters * 25) / 100, 2)


def elaborateTransaction(drink, moneyAmount):
    drinkCost = MENU[drink]["cost"]
    if moneyAmount < drinkCost:
        print(
            f"Sorry, not enough money inserted for a {drink}. Money refunded.")
        return False
    else:
        if moneyAmount > drinkCost:
            print(f"I give you back $ {moneyAmount - drinkCost}")
        resources["money"] += drinkCost
        return True


def prepareTheDrink(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if drink == "latte" or drink == "cappuccino":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    print(f"Drink purchased. Enjoy your {drink}.")


keepWorking = True
resources["money"] = 0

while keepWorking:
    choice = chooseDrink()
    if choice == "report":
        showReport()
    elif choice == "off":
        turnOff()
        keepWorking = False
    else:
        if resourcesAreEnough(choice):
            coinsInserted = getTheCoins(choice)
            if elaborateTransaction(choice, coinsInserted):
                prepareTheDrink(choice)
