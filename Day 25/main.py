import turtle
from scoreboard import Scoreboard
import pandas as pd

screen = turtle.Screen()
screen.title("US State game")
screen.setup(725, 491)
screen.addshape("Day 25/blank_states_img.gif")
turtle.shape("Day 25/blank_states_img.gif")

data = pd.read_csv("Day 25/50_states.csv")

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

scoreboard = Scoreboard()


def askForState(scoreboard):
    answer = screen.textinput(title=f"{scoreboard.score}/50 Guess the state",
                              prompt="What's another state name?").capitalize()

    if answer in data.state.tolist():
        showStateName(data[data.state == answer])
        scoreboard.score += 1


def showStateName(stateInfo):
    writer.goto(int(stateInfo.x), int(stateInfo.y))
    writer.write(f"{stateInfo.state.item()}", False, "center")


while scoreboard.score < 50:
    askForState(scoreboard)


screen.exitonclick()
