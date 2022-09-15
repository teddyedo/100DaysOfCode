from turtle import Screen
from snake import Snake

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey("Up")
screen.onkey("Down")
screen.onkey("Left")
screen.onkey("Right")

keepGoing = True

while keepGoing:
  screen.update()
  snake.move("forward")


screen.exitonclick()
