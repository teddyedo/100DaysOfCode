import turtle
import colorgram
from turtle import Turtle, Screen
import random as rd

myTurtle = Turtle()
colors = colorgram.extract("dots.jpg", 20)
rgbColors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgbColors.append((r, g, b))


for i in range(10):
    for j in range(10):
        color = rd.choice(rgbColors)
        myTurtle.color(color)
        myTurtle.fillcolor(color)
        myTurtle.begin_fill()
        myTurtle.circle(10)


myScreen = Screen()
myScreen.exitonclick()
