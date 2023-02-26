from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

my_screen = Screen()
my_screen.setup(height=600, width=1000)
my_screen.bgcolor("black")
my_screen.tracer(0)

my_paddle_a = Paddle((-480, 0))
my_paddle_b = Paddle((470, 0))
my_ball = Ball()
my_score = Score()

my_screen.listen()
my_screen.onkey(my_paddle_a.go_up, "Up")
my_screen.onkey(my_paddle_a.go_down, "Down")
my_screen.onkey(my_paddle_b.go_up, "w")
my_screen.onkey(my_paddle_b.go_down, "s")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    my_ball.move()
    # detect collision with top and bottom walls
    if my_ball.ycor() > 299 or my_ball.ycor() < -299:
        my_ball.change_y()

    # detect collision with side walls
    if my_ball.xcor() > 470:
        my_ball.back_to_center()
        my_score.score_update_a()
    if my_ball.xcor() < -470:
        my_ball.back_to_center()
        my_score.score_update_b()

    # detect collision with right paddle
    if my_ball.distance(my_paddle_b) < 50 and my_ball.xcor() > 450:
        my_ball.change_x()

    # detect collision with left paddle
    if my_ball.distance(my_paddle_a) < 50 and my_ball.xcor() > -470:
        my_ball.change_x()

my_screen.exitonclick()
