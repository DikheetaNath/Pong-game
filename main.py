# Importing classes
from turtle import Screen
from paddle import Paddle
from Ball import Ball
from scoreboard import Scoreboard
import time

# Screen Configuration:
screen = Screen()
screen.screensize(canvheight=600, canvwidth=800)
screen.bgcolor("black")
screen.title("--Pong Game--")
screen.tracer(8)

# Creating object
l_pad = Paddle(-350)
r_pad = Paddle(350)
ball = Ball()
l_score = Scoreboard(-100)
r_score = Scoreboard(100)

# Movement:
screen.listen()
screen.onkey(l_pad.move_up, "w")
screen.onkey(l_pad.move_down, "s")
screen.onkey(r_pad.move_up, "o")
screen.onkey(r_pad.move_down, "l")

game_is_on = True
ball_speed = 0.1


while game_is_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()

    # Detecting collisions with the wall:
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce('wall')

    # Detecting collision with paddles:
    if ball.xcor() < -335 and ball.distance(l_pad) < 50 or ball.xcor() > 335 and ball.distance(r_pad) < 50:
        ball.bounce('paddle')
        ball_speed *= 0.9

    # Detecting collision with vertical walls:
    if ball.xcor() > 360:
        ball.reset_pos()
        ball_speed = 0.1
        l_score.update_score(-100)

    elif ball.xcor() < -360:
        ball.reset_pos()
        ball_speed = 0.1
        r_score.update_score(100)


screen.exitonclick()
