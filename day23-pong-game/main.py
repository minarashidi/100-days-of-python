from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(False)  # Turn off the animation
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

right_paddle = Paddle("right")
left_paddle = Paddle("left")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.go_up)
screen.onkeypress(key="Down", fun=right_paddle.go_down)
screen.onkeypress(key="w", fun=left_paddle.go_up)
screen.onkeypress(key="s", fun=left_paddle.go_down)

is_game_on = True
while is_game_on:
    # make the ball move slower; Decrease the amount to make the ball move faster
    time.sleep(ball.speed_move)
    screen.update()
    ball.move()

    # Detect collision with the top and bottom walls; screen's height is 600.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_vertical()

    # Detect collision with paddles(measures the distance from the center of ball to the center of paddle)
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_horizontal()
        time.sleep(0.5)

    # Detect when the right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.update_left_score()

    # Detect when the left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.update_right_score()

screen.exitonclick()
