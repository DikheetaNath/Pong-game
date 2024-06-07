from turtle import Turtle
import random

X = random.randint(0, 360)


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.speed('fastest')
        self.xmove = 10
        self.ymove = 10

    def move(self):
        x = self.xcor() + self.xmove
        y = self.ycor() + self.ymove
        self.goto(x, y)

    def bounce(self, collision):
        if collision == 'wall':
            self.ymove *= -1
        else:
            self.xmove *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.xmove *= -1
        self.ymove *= -1