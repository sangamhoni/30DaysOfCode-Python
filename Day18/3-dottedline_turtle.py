import turtle
tim=turtle.Turtle()
screen=turtle.Screen()

for _ in range(10):
    tim.down()
    tim.forward(10)
    tim.up()
    tim.forward(10)


screen.exitonclick()