import random as rd
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.goto(rd.randint(-280, 280), rd.randint(-280, 280))

    def move(self):
        self.goto(rd.randint(-280, 280), rd.randint(-280, 280))
