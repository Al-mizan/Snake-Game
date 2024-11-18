from turtle import Turtle

class ScoreboardColor(Turtle):
    def __init__(self):
        super().__init__()
        self.fillcolor("DodgerBlue3")
        self.begin_fill()
        self.penup()
        self.goto(-400, 400)
        self.pendown()
        self.goto(400, 400)
        self.goto(400, 365)
        self.goto(-400, 365)
        self.goto(-400, 400)
        self.end_fill()
