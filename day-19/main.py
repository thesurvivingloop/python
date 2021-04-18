from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    heading = tim.heading()
    tim.setheading(heading + 10)


def turn_right():
    heading = tim.heading()
    tim.setheading(heading - 10)


def pen_up():
    tim.penup()


def pen_down():
    tim.pendown()


def clear_canvas():
    tim.clear()
    tim.reset()



screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="Up", fun=pen_up)
screen.onkey(key="Down", fun=pen_down)
screen.onkey(key="c", fun=clear_canvas)

screen.exitonclick()