from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.playerOneScore = 0
        self.playerTwoScore = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 265)
        self.writeScore()

    def writeScore(self):
        self.goto(-80, 270)
        self.write(self.playerOneScore, False,
                   "center", ("arial", 50, "bold"))
        self.goto(80, 270)
        self.write(self.playerTwoScore, False,
                   "center", ("arial", 50, "bold"))

    def update(self, playerNumber):
        if playerNumber == 1:
            self.playerOneScore += 1
        else:
            self.playerTwoScore += 1
        self.clear()
        self.writeScore()

    def gameEnded(self):
        return self.playerOneScore > 9 or self.playerTwoScore > 9
