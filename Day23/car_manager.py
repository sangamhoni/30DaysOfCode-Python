COLORS = ['#CCE1F2', '#C6F8E5', '#FBF7D5', '#F9DED7', '#F5CDDE', '#E2BEF1', '#F1E6B2', '#DF8877', '#A6B8C1', '#B3B995',
          '#E1B87F', '#C6B0BC']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random


class CarManager():
    def __init__(self):
        # super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_pos = random.randint(-230, 250)
            new_car.penup()
            new_car.setpos(320, y_pos)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            if car.xcor() > -320:
                car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
