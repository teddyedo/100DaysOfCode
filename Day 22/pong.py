from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

WIDTH = 1000
HEIGHT = 700


def createDivisor():
    divisor = Turtle()
    divisor.speed(0)
    divisor.penup()
    divisor.goto(0, HEIGHT / 2)
    divisor.setheading(270)
    divisor.color("white")
    divisor.pensize(3)
    divisor.hideturtle()

    while divisor.ycor() > -(HEIGHT / 2):
        divisor.pendown()
        divisor.fd(20)
        divisor.penup()
        divisor.fd(20)


screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

createDivisor()

scoreboard = Scoreboard()

leftPaddle = Paddle(-450)
rightPaddle = Paddle(450)

screen.listen()
screen.onkeypress(leftPaddle.up, "w")
screen.onkeypress(leftPaddle.down, "s")
screen.onkeypress(rightPaddle.up, "Up")
screen.onkeypress(rightPaddle.down, "Down")


ball = Ball()

keepGoing = True


while keepGoing:
    time.sleep(ball.speed)
    screen.update()

    ball.move()

    if ball.collide():
        ball.bounce(1, -1)

    if (ball.distance(rightPaddle) < 50 and ball.xcor() > 430) or (ball.distance(leftPaddle) < 50 and ball.xcor() < -430):
        ball.bounce(-1, 1)
        ball.speed * 0.9

    if ball.xcor() > 500:
        scoreboard.update(1)
        ball.restart()
    elif ball.xcor() < -500:
        scoreboard.update(2)
        ball.restart()


screen.exitonclick()
