from lib2to3.pgen2.token import NUMBER
from car import Car
import random as rd

NUMBER_OF_CARS = 20


class CarManager():

    def __init__(self):
        self.cars = []
        self.numberOfCars = NUMBER_OF_CARS
        self.generateCars()

    def generateCars(self):
        self.deleteCars()
        for _ in range(self.numberOfCars):
            self.createCar()

    def createCar(self):
        car = Car()
        car.goto(rd.randint(-250, 250), rd.randint(-250, 250))
        self.cars.append(car)

    def moveCars(self):
        for car in self.cars:
            car.move()

    def updateDifficult(self):
        self.numberOfCars += 1
        self.generateCars()
        for car in self.cars:
            car.incrementSpeed()

    def deleteCars(self):
        for car in self.cars:
            car.reset()
            car.hideturtle()
        self.cars = []

    def hitPlayer(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False
