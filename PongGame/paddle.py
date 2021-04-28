from turtle import Turtle

MOVE_DISTANCE = 30


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        y_cor = self.ycor()
        x_cor = self.xcor()
        y_cor_new = y_cor + MOVE_DISTANCE

        if y_cor_new <= 250:
            self.goto(x_cor, y_cor_new)

    def down(self):
        y_cor = self.ycor()
        x_cor = self.xcor()
        y_cor_new = y_cor - MOVE_DISTANCE

        if y_cor_new >= -250:
            self.goto(x_cor, y_cor_new)






