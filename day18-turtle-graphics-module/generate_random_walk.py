import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()

named_colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
                "SeaGreen"]


def random_color():
    """Returns a 3-tuple of random numbers in the range 0 - 255
    eg : (89, 103, 108)"""
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    random_rgb = (red, green, blue)
    return random_rgb


# Define possible directions for the random walk: # 0 will be facing East and then 90 will be facing North, 180 will be West and 270 will be South.
random_direction = [0, 90, 180, 270]

# Perform the random walk
for _ in range(100):
    # tim.color(random.choice(named_colors))
    tim.color(random_color())

    # Set the line thickness
    tim.pensize(15)

    # Set the drawing speed to the fastest
    tim.speed("fastest")

    # Move the turtle forward by 30 units
    tim.forward(30)

    # Set a random heading for the turtle
    tim.setheading(random.choice(random_direction))

screen = turtle.Screen()
screen.exitonclick()
