from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, startX):
        super().__init__()
        self.shapesize(5, 0.5)
        self.penup()
        self.color("white")
        self.shape("square")
        self.setx(startX)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
