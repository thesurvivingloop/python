from turtle import Turtle

MOVE = False
ALIGNMENT = "Center"
FONT = "Courier"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-40, 275)
        self.color("white")
        self.score_left_paddle = 0
        self.score_right_paddle = 0
        self.hideturtle()
        self.write("Score", align=ALIGNMENT, move=MOVE, font=FONT)
        self.setheading(270)
        self.forward(20)
        self.write(f"{self.score_left_paddle} - {self.score_right_paddle}", align=ALIGNMENT, move=MOVE, font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"{self.score_left_paddle} - {self.score_right_paddle}", align=ALIGNMENT, move=MOVE, font=FONT)

    def game_over(self):
        self.goto((0, 0))
        self.write("GAME OVER.", align=ALIGNMENT, move=MOVE, font=FONT)


