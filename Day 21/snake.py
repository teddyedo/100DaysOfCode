from turtle import Turtle
import time

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.createSnake()
        self.head = self.segments[0]

    def createSnake(self):
        for pieceOfTheSnake in range(3):
            myTurtle = Turtle()
            myTurtle.penup()
            myTurtle.shape("square")
            myTurtle.color("white")
            myTurtle.setx(myTurtle.xcor() - 20 * pieceOfTheSnake)
            self.segments.append(myTurtle)

    def move(self):
        time.sleep(0.1)
        for segmentNumber in range(len(self.segments) - 1, 0, -1):
            nextX = self.segments[segmentNumber - 1].xcor()
            nextY = self.segments[segmentNumber - 1].ycor()
            self.segments[segmentNumber].goto(nextX, nextY)
        self.head.fd(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def eat(self):
        myTurtle = Turtle()
        myTurtle.penup()
        myTurtle.shape("square")
        myTurtle.color("white")
        myTurtle.goto(self.segments[-1].position())
        self.segments.append(myTurtle)

    def eatItself(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False
