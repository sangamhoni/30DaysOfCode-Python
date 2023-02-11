from turtle import Turtle
ALIGNMENT='center'
FONT_STYLE=('Courier', 15, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setpos(0, 270)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT_STYLE)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT_STYLE)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT_STYLE)



