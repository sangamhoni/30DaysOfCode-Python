from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(0.5)
        self.speed('fastest')
        self.refresh_food()

    def refresh_food(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.setpos(random_x, random_y)
