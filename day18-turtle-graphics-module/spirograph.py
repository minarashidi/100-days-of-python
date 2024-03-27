import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    random_rgb = (red, green, blue)
    return random_rgb


# Draw a circle
tim.color(random_color())
tim.speed("fastest")


def draw_spirograph(offset):
    """
    Draw a number of circles each with a radius of 100 in distance
    """
    for i in range(0, int(360 / offset)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + offset)


draw_spirograph(20)

screen = t.Screen()
screen.exitonclick()
