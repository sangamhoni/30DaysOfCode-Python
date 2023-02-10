from turtle import Turtle, Screen

tim=Turtle()
screen=Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def rotate_left():
    tim.left(10)

def rotate_right():
    tim.right(10)

def pen_updown():
    if tim.isdown():
        tim.penup()
    else:
        tim.pendown()

def clear_screen():
    tim.clear()
    # you can simply use tim.home() instead of this
    tim.penup()
    tim.setpos(0, 0)
    tim.pendown()

screen.listen()
screen.onkeypress(key='w', fun=move_forward)
screen.onkeypress(key='s', fun=move_backward)
screen.onkeypress(key='a', fun=rotate_left)
screen.onkeypress(key='d', fun=rotate_right)
screen.onkey(key='space', fun=pen_updown)
screen.onkey(key='c', fun=clear_screen)

screen.exitonclick()
