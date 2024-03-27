from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")

# draw a square
for _ in range(4):
    tim.forward(50)
    tim.right(90)

# draw a dashed line
for _ in range(10):
    tim.forward(10)
    # Pull the pen up – no drawing when moving.
    tim.penup()
    tim.forward(10)
    # Pull the pen down – drawing when moving.
    tim.pendown()


# draw different shapes: triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon.
def draw_shape(number_of_sides):
    for i in range(number_of_sides):
        angle = 360 / number_of_sides
        tim.forward(100)
        tim.right(angle)


colors = ["red", "blue", "green", "cyan", "wheat", "black", "pink", "DarkOrange1", "brown4"]
for sides in range(3, 10):
    tim.color(random.choice(colors))
    draw_shape(sides)

screen = Screen()
screen.exitonclick()
