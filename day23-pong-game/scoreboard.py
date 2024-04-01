from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.right_score = 0
        self.left_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(100, 220)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)
        self.goto(-100, 220)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)

    def update_right_score(self):
        self.right_score += 1
        self.update_scoreboard()

    def update_left_score(self):
        self.left_score += 1
        self.update_scoreboard()
