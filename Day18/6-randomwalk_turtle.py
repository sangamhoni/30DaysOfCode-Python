import random
import turtle
tim=turtle.Turtle()
screen=turtle.Screen()

turtle.colormode(255)

def random_color():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    return (r, g, b)

direction=[90, 180, 270, 360]
tim.pensize(13)
tim.speed('fastest')

while True:
    tim.color(random_color())
    tim.forward(30)
    tim.right(random.choice(direction))






screen.exitonclick()