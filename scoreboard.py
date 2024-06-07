from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, x):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(x, 200)
        self.write(self.score, font=('Ariel', 20, 'normal'))

    def update_score(self, x):
        self.score += 1
        self.clear()
        self.goto(x, 200)
        self.write(self.score, font=('Ariel', 20, 'normal'))

