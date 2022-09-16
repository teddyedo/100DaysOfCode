from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 265)
        self.write(f"Score: {self.score}", False,
                   "center", ("arial", 20, "bold"))

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False,
                   "center", ("arial", 20, "bold"))

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game over.", False, "center", ("arial", 20, "normal"))
