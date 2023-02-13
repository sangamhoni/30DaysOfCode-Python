from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        # self.sign=choice([True, False])

        # function to add direction of where the ball should go
        # self.direction=random.choice((10, -10))
        self.shoot_ball(random.choice((10, -10)))


    def move(self):
        new_x=self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def shoot_ball(self, ball_direction):
        self.setpos(0, 0)
        self.direction = ball_direction
        self.x_move=self.direction
        self.y_move=random.choice((10, -10))



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
