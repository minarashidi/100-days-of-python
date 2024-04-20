import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
states_image = "blank_states_img.gif"
screen.addshape(states_image)
turtle.shape(states_image)

data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(f"{len(guessed_states)}/50 States Correct", "What's another state name?").title()
    if user_answer == "Exit":
        missed_states = []
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)

        df = pd.DataFrame(missed_states)
        df.to_csv("missed_states.csv")
        break
    if user_answer in all_states:
        guessed_states.append(user_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row = data[data["state"] == user_answer]
        t.goto(int(state_row.x.item()), int(state_row.y.item()))
        t.write(state_row.state.item())

screen.exitonclick()
