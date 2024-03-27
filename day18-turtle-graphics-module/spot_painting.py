import turtle as t
import colorgram  # A Python library that lets you extract colors from images
import random

t.colormode(255)
colors = colorgram.extract('hirst_spot_painting.png', 10)
# for color in colors:
#     red = color.rgb.r
#     green = color.rgb.g
#     blue = color.rgb.b
#     random_rgb = (red, green, blue)
#     color_list.append(random_rgb)
# print(color_list)
tim = t.Turtle()
color_list = [(240, 242, 245), (223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159),
              (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93)]


def draw_dotted_line():
    """Draw 10 dots in each line"""
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(30)


tim.penup()
# Starting position
tim.goto(-100, -100)

# Draw the dots; Iterate 10 times for 10 lines
for _ in range(10):
    draw_dotted_line()
    tim.setpos(-100, tim.ycor() + 30)  # Move to the next line

tim.hideturtle()
t.Screen().exitonclick()
