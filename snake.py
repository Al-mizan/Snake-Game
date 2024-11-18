from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        x = 0
        for _ in range(3):
            self.add_one_segment((x,0))
            x -= 20

    def add_one_segment(self, pos):
        snake = Turtle('square')
        self.snakes.append(snake)
        snake.penup()
        snake.color('grey17')
        snake.setpos(pos)

    def add_snake(self):
        self.add_one_segment(self.snakes[-1].position())

    def go_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        length = len(self.snakes)
        for i in range(length - 1, 0, -1):
            x = self.snakes[i - 1].xcor()
            y = self.snakes[i - 1].ycor()
            self.snakes[i].goto(x, y)
        self.head.forward(MOVE_DISTANCE)