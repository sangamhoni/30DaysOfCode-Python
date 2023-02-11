import turtle
from turtle import Screen
import time
from snake_class import Snake
from food import Food
from scoreboard import Score

screen=Screen()
# screen.screensize(WIDTH, HEIGHT)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# to turn off the display so that nothing is seen at first
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Score()

screen.listen()
screen.onkey(key='w', fun=snake.up)
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='s', fun=snake.down)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='a', fun=snake.left)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='d', fun=snake.right)
screen.onkey(key='Right', fun=snake.right)

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()

#     detect eating food
    if snake.head.distance(food)<10:
        food.refresh_food()
        snake.extend()
        scoreboard.increase_score()

#     detect collision with wall
    if snake.head.xcor()>289 or snake.head.xcor()< -290 or snake.head.ycor()>290 or snake.head.ycor()< -290:
        game_is_on=False
        scoreboard.game_over()

#         detect collision with tail
#     slicing
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<5:
            game_is_on=False
            scoreboard.game_over()

screen.exitonclick()