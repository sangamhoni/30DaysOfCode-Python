from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import random
import time

# screen setup
screen=Screen()
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


# creating and moving paddles
screen.listen()
# right paddle
r_paddle=Paddle((350, 0))
screen.onkeypress(key='Up', fun=r_paddle.move_up)
screen.onkeypress(key='Down', fun=r_paddle.move_down)

# left paddle
l_paddle=Paddle((-350, 0))
screen.onkeypress(key='w', fun=l_paddle.move_up)
screen.onkeypress(key='s', fun=l_paddle.move_down)

# creating ball and scoreboard
ball=Ball()
score=ScoreBoard()

BALL_SPEED=0.07

game_is_on=True
while game_is_on:
    time.sleep(BALL_SPEED)
    screen.update()
    ball.move()

#   detect collision with wall
    if ball.ycor()>280 or ball.ycor()< -270:
        ball.wall_bounce()

#   detect collision with paddle
    if ball.xcor()==330 or ball.xcor() == -330:
        if ball.distance(l_paddle)<75 or ball.distance(r_paddle)<75:
            ball.paddle_bounce()
            if BALL_SPEED>0.035:
                BALL_SPEED-=0.005

    # detect missed ball
    if ball.xcor() == 420 or ball.xcor() == -420:
        if ball.xcor() == 420:
            score.l_point()
            ball.shoot_ball(-10)
        else:
            score.r_point()
            ball.shoot_ball(10)

        BALL_SPEED=0.1
        screen.update()
        time.sleep(1)

        # game_is_on=False

# screen.exitonclick()
