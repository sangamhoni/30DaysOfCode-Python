import turtle
import time
import random

WIDTH, HEIGHT = 600, 650
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']


def get_number_of_racers():
    total_turtle = 0
    while True:
        total_turtle = input("Enter number of racers (2-10): ")
        if total_turtle.isdigit():
            total_turtle = int(total_turtle)
        else:
            print("Invalid entry! Try again")
            continue

        if 2 <= total_turtle <= 10:
            return total_turtle
        else:
            print("Numbers not in range 2-10. Try again")


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 20:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    for i in range(len(colors)):
        spacingx = WIDTH // (len(colors) + 1) * (i + 1)
        racer = turtle.Turtle()
        racer.color(colors[i])
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        # setting position
        racer.setpos(spacingx - (WIDTH // 2), 20 - (HEIGHT // 2))
        racer.pendown()
        turtles.append(racer)

    return turtles


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racer")


racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
time.sleep(2)
print(f"The winner is the turtle with color: {winner}")
