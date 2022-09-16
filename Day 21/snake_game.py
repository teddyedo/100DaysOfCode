from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()

scoreboard = Scoreboard()

keepGoing = True

while keepGoing:
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        snake.eat()
        food.move()
        scoreboard.update()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        keepGoing = False
        scoreboard.gameOver()

    if snake.eatItself():
        keepGoing = False
        scoreboard.gameOver()


screen.exitonclick()
