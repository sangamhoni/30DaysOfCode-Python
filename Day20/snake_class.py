import turtle
STARTING_POSITION=[(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE=10
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
        # self.head.color("yellow")

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = turtle.Turtle('square')
        new_segment.color("white")
        new_segment.shapesize(0.5, 0.5)
        # after changing shapesize to 0.5, the new segment size is 10px X 10px
        new_segment.penup()
        new_segment.setpos(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x, new_y = self.segments[seg_num - 1].pos()
            self.segments[seg_num].setpos(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)