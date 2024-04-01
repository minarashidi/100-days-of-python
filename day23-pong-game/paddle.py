from turtle import Turtle

POSITION = {"right": (350, 0), "left": (-350, 0)}


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)  # 100*20
        self.color("white")
        self.goto(POSITION[position])

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() + -20)
