from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

print(logo)


def calculator():
    num1 = float(input("What's the first number? "))

    for symbol in operations:
        print(symbol)

    keepGoing = True

    while keepGoing:
        operation = input("Which operation do you want? ")
        num2 = float(input("What's the next number? "))
        result = operations[operation](num1, num2)
        print(f"The result is {result}")

        userChoice = input(
            "Do you want to continue with {result} and another operation? (y or n): ")
        if userChoice == "n":
            keepGoing = False
            calculator()
        else:
            num1 = result


calculator()
