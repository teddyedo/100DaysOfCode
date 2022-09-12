from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def chooseDrink():
    return input("What would you like? (espresso/latte/cappuccino): ")


coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

keepGoing = True
while keepGoing:
    choice = chooseDrink()
    if choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif choice == "off":
        keepGoing = False
    else:
        drink = Menu().find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)
