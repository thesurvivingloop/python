from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 275)
        self.color("yellow")
        self.font = ("Courier", 15, "normal")
        self.score_text = f"Score : {self.score}"
        self.hideturtle()
        self.write(self.score_text, False, align="center", font=self.font)

    def update_score(self):
        self.score += 1
        self.score_text = f"Score : {self.score}"
        self.clear()
        self.write(self.score_text, False, align="center", font=self.font)

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("GAME OVER.", False, align="center", font=self.font)


