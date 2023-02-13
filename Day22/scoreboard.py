from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update_score()


    def update_score(self):
        self.clear()
        self.setpos(-90, 240)
        self.write(self.l_score, align='center', font=('Futura', 35, 'bold'))
        self.setpos(90, 240)
        self.write(self.r_score, align='center', font=('Futura', 35, 'bold'))

    def l_point(self):
        self.l_score+=1
        self.update_score()

    def r_point(self):
        self.r_score+=1
        self.update_score()
