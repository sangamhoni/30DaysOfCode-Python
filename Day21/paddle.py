from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, paddle_position):
        super().__init__()
        self.shape('square')
        self.color('white')
        # self.tilt(90)
        self.shapesize(5, 1)
        # 1x width(100px) and 5x length(20px)
        self.penup()
        self.setpos(paddle_position)


    def move_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(), new_y)


    def move_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(), new_y)
