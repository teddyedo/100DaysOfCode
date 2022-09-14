from turtle import Turtle, Screen
import random as rd

isRaceOn = False
HEIGHT = 400
WIDTH = 500

screen = Screen()
screen.setup(WIDTH, HEIGHT)
userChoice = screen.textinput(
    "Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

y = 150

for color in colors:

    newTurtle = Turtle(shape="turtle")
    newTurtle.color(color)
    newTurtle.penup()
    newTurtle.goto(-230, y)
    y -= 60
    turtles.append(newTurtle)

if userChoice:
    isRaceOn = True

winner = ""

while isRaceOn:
    for turtle in turtles:
        turtle.fd(rd.randint(1, 10))
        if turtle.xcor() > WIDTH / 2 - 20:
            isRaceOn = False
            winner = turtle.color()[0]
if winner == userChoice:
    print("Your bet was right!")
else:
    print(f"You lost. The winner is {winner}")

screen.exitonclick()
