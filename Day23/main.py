import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

tim = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key='Up', fun=tim.move_up)
screen.onkeypress(key='Down', fun=tim.move_down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    #     detect collision with car
    for car in car_manager.cars:
        if car.distance(tim) < 20:
            scoreboard.game_over()
            game_is_on = False

    #     detect successful crossing
    if tim.is_at_finish_line():
        car_manager.level_up()
        scoreboard.increase_level()
        tim.goto_start()

screen.exitonclick()
