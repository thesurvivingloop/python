from turtle import Turtle, Screen
from turtle import colormode
import random

colormode(255)
colors = ["red", "blue", "black", "green", "yellow", "orange"]
screen = Screen()
screen.setup(width=500, height=400)


def turtles_get_ready(all_turtles):
    x = -220
    y = (len(all_turtles) / 2) * 40
    for turtle in all_turtles:
        turtle.goto(x, y)
        y -= 40


def generate_turtles():
    turtles = []
    for i in range(6):
        turtles.append(Turtle(shape="turtle"))
        # turtles[i].shape("turtle")
        turtles[i].speed("slow")
        turtles[i].penup()
        turtles[i].color(colors[i])
    return turtles


def conduct_race(all_turtles):
    race_still_on = True
    while race_still_on:
        for turtle in all_turtles:
            turtle.forward(random.randint(0, 20))
            if turtle.xcor() >= 230:
                race_still_on = False
                print(f"winner x_cor = {turtle.xcor()}")
                return turtle


race_turtles = generate_turtles()
turtles_get_ready(race_turtles)

user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
print(user_bet)

winner = conduct_race(race_turtles)
winning_color = winner.pencolor()

if winning_color == user_bet:
    print("You won!!")
else:
    print("You lost..")
print(f"The winning turtle is {winning_color}")

screen.exitonclick()