from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x):
        super().__init__()
        self.color('white')
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=4)
        self.penup()
        self.goto(x, 0)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)