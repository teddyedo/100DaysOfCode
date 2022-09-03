from alphabet import alphabet
from art import logo


def caesar(text, shift, typeOfElaboration):
    elaboratedText = ""
    if typeOfElaboration == "decode":
        shift = -shift

    for letter in text:
        if letter in alphabet:
            elaboratedText += alphabet[(alphabet.index(letter) +
                                        shift) % len(alphabet)]
        else:
            elaboratedText += letter
    print(f"The {typeOfElaboration}d text is {elaboratedText}")


print(logo)

keepGoing = "yes"

while keepGoing == "yes":
    typeOfElaboration = input("What you want to do? (encode or decode): ")
    text = input(f"Type the text you want to {typeOfElaboration}: ").lower()
    shift = int(input("How much you want to shift?: "))
    caesar(text, shift, typeOfElaboration)

    keepGoing = input("Do you want to continue? (yes or no): ").lower()
