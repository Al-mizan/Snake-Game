from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0,365)
        self.hideturtle()
        self.score(0)

    def score(self, number):
        self.clear()
        self.write(f'Score : {number}', align='center', font=('Courier', 18, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over!', align='center', font=('Courier', 22, 'bold'))
