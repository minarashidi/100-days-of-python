from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake(object):

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        # In Python we can write -1, to count from the end of the list
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            previous_segment = self.segments[segment_index - 1]
            current_segment = self.segments[segment_index]
            current_segment.goto(previous_segment.xcor(),
                                 previous_segment.ycor())  # moving the last segment to the previous one

        self.head.forward(MOVE_DISTANCE)

        # To move the snake, the head needs to change direction; it can't go both forward and backward.

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
