from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.xMove = 5
        self.yMove = 5
        self.speed = 0.03

    def move(self):
        self.goto(self.xcor() + self.xMove, self.ycor() + self.yMove)

    def collide(self):
        return self.ycor() >= 340 or self.ycor() <= -340

    def bounce(self, xdir, ydir):
        self.xMove *= xdir
        self.yMove *= ydir

    def restart(self):
        self.goto(0, 0)
        self.bounce(-1, 1)
        self.speed = 0.03
