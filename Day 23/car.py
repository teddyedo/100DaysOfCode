from turtle import Turtle
import random as rd

CAR_SPEED = 5
CAR_SPEED_INCREMENT = 2


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed = CAR_SPEED
        self.setheading(180)
        self.color((rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255)))
        self.shape("square")
        self.shapesize(1, 2)

    def move(self):
        self.fd(self.speed)
        if self.xcor() < -320:
            self.restart()

    def incrementSpeed(self):
        self.speed += CAR_SPEED_INCREMENT

    def restart(self):
        self.setx(300)
