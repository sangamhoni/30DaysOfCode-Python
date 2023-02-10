import turtle
import time
from snake_class import Snake

screen=turtle.Screen()
# screen.screensize(WIDTH, HEIGHT)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# to turn off the display so that nothing is seen at first
screen.tracer(0)

snake=Snake()

screen.listen()
screen.onkey(key='w', fun=snake.up)
screen.onkey(key='s', fun=snake.down)
screen.onkey(key='a', fun=snake.left)
screen.onkey(key='d', fun=snake.right)

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

# screen.exitonclick()