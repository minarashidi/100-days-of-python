from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speed_move = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_vertical(self):
        self.y_move *= -1

    def bounce_horizontal(self):
        """ It means that the ball touches by the paddle and should bounce the other side with a bit faster speed."""
        self.x_move *= -1
        self.speed_move *= 0.7

    def reset_position(self):
        self.goto(0, 0)
        self.speed_move = 0.1
        # Reverse the X axis; when the paddle misses the ball, we should reverse the position and the ball bounces the other side.
        self.bounce_horizontal()
