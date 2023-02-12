from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
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

# creating ball
ball=Ball()

game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

#     detect collision with wall
    if ball.ycor()>280 or ball.ycor()< -280:
        ball.bounce()


screen.exitonclick()
