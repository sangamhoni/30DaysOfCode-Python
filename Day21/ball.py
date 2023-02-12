from turtle import Turtle
from random import choice

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        # self.sign=choice([True, False])
        self.x_move=10
        self.y_move=10


    def move(self):
        new_x=self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move *= -1

    # # YOU CAN DO THIS TO DETECT COLLISION TOO
    # def move(self):
    #     x_cor=self.xcor()+10
    #     y_cor = self.ycor()
    #
    #     if y_cor>=280:
    #         self.sign=True
    #     elif y_cor<= -280:
    #         self.sign=False
    #     if self.sign==True:
    #         y_cor-=10
    #     else:
    #         y_cor+=10
    #
    #     self.goto(x_cor,y_cor)
