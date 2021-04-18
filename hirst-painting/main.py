import colorgram
from turtle import Turtle
from turtle import Screen
import random
from turtle import colormode

colormode(255)
number_of_colors = 50
# colors = colorgram.extract("hirst_painting.jpeg", number_of_colors)
colors = colorgram.extract("DHS8614againstwall_771_0.jpeg", number_of_colors)
print(len(colors))
colors_list = []
for i in colors:
    red = i.rgb.r
    blue = i.rgb.b
    green = i.rgb.g
    # if statement added to avoid lighter colors since the background is white
    if not (red > 230 or green > 230 or blue > 230):
        color_tuple = (red, blue, green)
        colors_list.append(color_tuple)


def set_initial_position(tim_myturtle):
    tim_myturtle.setheading(225)
    tim_myturtle.forward(250)
    tim_myturtle.setheading(0)


def draw_dotted_line(tim_turtle, number_of_dots, radius):
    for dot in range(number_of_dots):
        color = random.choice(colors_list)
        tim_turtle.dot(radius, color)
        if dot < number_of_dots - 1:
            tim_turtle.forward(2.5 * radius)


def take_position_for_line(direction, radius):
    tim.setheading(90)
    tim.forward(radius * 2.5)
    if direction == "backwards":
        tim.setheading(180)
    elif direction == "forward":
        tim.setheading(0)


tim = Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fastest")
number_of_lines = 40
radius_dot = 7
number_of_dots_per_line = 40

set_initial_position(tim)
for i in range(1, number_of_lines+1):
    draw_dotted_line(tim, number_of_dots_per_line, radius_dot)
    if i % 2 != 0:
        take_position_for_line("backwards", radius_dot)
    else:
        take_position_for_line("forward", radius_dot)
my_canvas = Screen()
my_canvas.exitonclick()
