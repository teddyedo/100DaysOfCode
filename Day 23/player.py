from turtle import Turtle

MOVE_DISTANCE = 10
STARTING_POSITION = (0, -280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.color("green")
        self.shape("turtle")
        self.goto(STARTING_POSITION)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def isArrived(self):
        return self.ycor() > 290

    def restart(self):
        self.goto(STARTING_POSITION)
