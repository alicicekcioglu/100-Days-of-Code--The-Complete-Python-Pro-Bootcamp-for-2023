from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

# Screen
screen = Screen()
screen.tracer(0)
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
score = Scoreboard()

# create paddles
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

# left/right move
screen.listen()
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(left_paddle.go_up, "w")

# Create ball
ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect ball misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.left_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.right_point()

screen.exitonclick()
