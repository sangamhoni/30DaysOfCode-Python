import random
import turtle
tim=turtle.Turtle()
screen=turtle.Screen()

colors=['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGrey', 'SeaGreen']
random.shuffle(colors)

tim.pensize(3)
for side in range(3, 11):
    tim.color(colors[side-3])
    exterior_angle=360/side
    for _ in range(side):
        tim.forward(100)
        tim.right(exterior_angle)





screen.exitonclick()