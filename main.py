from turtle import Screen
from time import sleep

from snake import Snake
from food import Food
from scoreboard import Scoreboard
from scoreboardcolor import ScoreboardColor

screen = Screen()
screen.setup(width=800, height=800)
screen.title("Snake Game")
screen.bgcolor('lightblue4')
screen.tracer(0)

scoreboard_color = ScoreboardColor()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.go_up, 'Up')
screen.onkey(snake.go_down, 'Down')
screen.onkey(snake.go_left, 'Left')
screen.onkey(snake.go_right, 'Right')

game_is_on = True
points = 0

while game_is_on:

    screen.update()
    sleep(0.09)
    snake.move()

    if snake.head.distance(food) <= 15:
        snake.add_snake()
        food.new_position()
        points += 1
        scoreboard.score(points)

    if snake.head.xcor() > 397 or snake.head.xcor() < -397 or snake.head.ycor() < -397 or snake.head.ycor() > 365:
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()