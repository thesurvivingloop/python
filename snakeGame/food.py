from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        x_remainder = random_x % 20
        y_remainder = random_y % 20
        random_x -= x_remainder
        random_y -= y_remainder
        self.goto(random_x, random_y)
