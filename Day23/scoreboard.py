FONT = ("Courier", 15, "normal")

from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color('white')
        self.setpos(-280, 260)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", align='left', font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", align='center', font=FONT)
