STARTING_POSITION = (0, -275)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('#77f995')
        self.setheading(90)
        self.penup()
        self.goto_start()
        # self.

    def move_up(self):
        if self.ycor() < 280:
            self.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > -275:
            self.backward(MOVE_DISTANCE)

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
