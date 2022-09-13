import colorgram
import turtle as turtle
import random as rd

myTurtle = turtle.Turtle()
colors = colorgram.extract("dots.jpg", 20)
rgbColors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgbColors.append((r, g, b))

turtle.colormode(255)
myTurtle.speed(0)
myTurtle.penup()
myTurtle.hideturtle()

myTurtle.setheading(225)
myTurtle.fd(300)
myTurtle.setheading(0)
numberOfDots = 100

for dot in range(1, numberOfDots + 1):
    myTurtle.dot(20, rd.choice(rgbColors))
    myTurtle.fd(50)

    if dot % 10 == 0:
      myTurtle.setheading(90)
      myTurtle.fd(50)
      myTurtle.setheading(180)
      myTurtle.fd(500)
      myTurtle.setheading(0)

myScreen = turtle.Screen()
myScreen.exitonclick()
