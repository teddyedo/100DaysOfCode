from turtle import Turtle

FONT = ("Arial", 17, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-250, 260)
        self.writeLevel()

    def writeLevel(self):
        self.clear()
        self.write(f"Level: {self.level}", False,  "center", FONT)

    def updateLevel(self):
        self.level += 1
        self.writeLevel()

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game over", False, "center", FONT)
