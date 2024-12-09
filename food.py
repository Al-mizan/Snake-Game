from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('red')
        self.shape('circle')
        self.shapesize(0.5, 0.5)
        self.speed('fastest')
        self.new_position()

    def new_position(self):
        x = randint(-380,380)
        y = randint(-380,360)
        self.goto(x,y)
