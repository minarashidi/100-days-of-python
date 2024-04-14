from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

"""
The player is the turtle which will cross the road
"""


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start_position()

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_successful_crossing(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def go_to_start_position(self):
        self.goto(STARTING_POSITION)
