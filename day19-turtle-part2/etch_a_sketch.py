from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


def move_backward():
    tim.backward(20)


def turn_left():
    tim.setheading(tim.heading() + 10)
    # tim.left(20)


def turn_right():
    tim.setheading(tim.heading() - 10)
    # tim.right(20)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
