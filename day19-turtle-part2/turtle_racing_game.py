from turtle import Turtle, Screen
import turtle
import random

"""
popup: Make your bet
prompt: input("Who will win the race? Enter a color:")

Once I click "OK", all our turtles line up in the starting position and begin making random steps towards the right edge of the screen.
When the first turtle crosses the finish line, it will print out whether we won or lost our bet and which turtle won the game.
Set the colors for drawing
"""

colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
turtles = []

screen = Screen()
screen.setup(width=500, height=400)
user_bet = turtle.textinput("Make your bet", "Who will win the race? Enter a color:")


def line_up_turtles():
    y_position = [-100, -70, -40, -10, 20, 50, 80]
    for turtle_index in range(0, 6 + 1):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-200, y=y_position[turtle_index])
        turtles.append(new_turtle)


def start_race():
    is_game_over = False
    finish_x_position = 230
    while not is_game_over:
        for t in turtles:
            if t.xcor() > finish_x_position:
                is_game_over = True
                winner_color = t.pencolor()
                if user_bet == winner_color:
                    print(f"You've won! The winner color is {winner_color} ")
                else:
                    print(f"You've lost! The winner color is {winner_color} ")
            else:
                t.forward(random.randint(0, 10))


line_up_turtles()
start_race()
screen.exitonclick()
