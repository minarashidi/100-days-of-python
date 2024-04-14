from turtle import Turtle

FONT = ("Courier", 24, "normal")

"""
Write the level that we are currently in and the game over sequence
"""


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("red")
        self.penup()
        self.goto(-280, 260)
        self.update_level()

    def update_level(self):
        self.write(f"Level = {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", font=FONT)
