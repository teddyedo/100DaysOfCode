from turtle import Screen, Turtle

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard
import time

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.tracer(0)
screen.setup(WIDTH, HEIGHT)
screen.colormode(255)

scoreboard = Scoreboard()
player = Player()
carManager = CarManager()

screen.listen()
screen.onkeypress(player.move, "Up")

keepGoing = True

while keepGoing:
    screen.update()
    time.sleep(0.1)
    carManager.moveCars()

    if player.isArrived():
        player.restart()
        scoreboard.updateLevel()
        carManager.updateDifficult()

    if carManager.hitPlayer(player):
        keepGoing = False
        scoreboard.gameOver()

screen.exitonclick()
