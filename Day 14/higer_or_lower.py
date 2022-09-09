from calendar import c
from art import logo
from art import vs
from data import data
import random as rd


def showVipInfo(firstVip, secondVip):

    print(
        f"\nOption A: {firstVip['name']}, {firstVip['description']}, {firstVip['country']}")
    print(vs)
    print(
        f"Option B: {secondVip['name']}, {secondVip['description']}, {secondVip['country']}\n")


def pickAVip():
    pos = rd.randint(0, len(data) - 1)
    vipInfo = data[pos]
    data.pop(pos)
    return vipInfo


def choiceCorrect(choice, firstVip, secondVip):
    if choice == "A" and firstVip["follower_count"] >= secondVip["follower_count"]:
        return True
    elif choice == "B" and secondVip["follower_count"] >= firstVip["follower_count"]:
        return True
    else:
        return False


def playATurn(firstVip):
    global score
    secondVip = pickAVip()
    showVipInfo(firstVip, secondVip)
    choice = input(("Which one has more followers on Instagram? (A or B): "))
    if choiceCorrect(choice, firstVip, secondVip):
        print(
            f"That's right! {secondVip['name']} has {secondVip['follower_count']} million followers. go on with the next one.")
        score += 1
        if score == 49:
            print("Congratulation! You won the game!!!")
        else:
            playATurn(secondVip)
    else:
        print(
            f"That's wrong! {secondVip['name']} has {secondVip['follower_count']} million followers. Your final score is {score}")


print(logo)
print("Welcome to the Higer or Lower game! You have to tell me, choosing between 2 famous people, which one has the most followers on instagram")
score = 0

playATurn(pickAVip())
