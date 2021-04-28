from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

MOVE_DISTANCE = 20

game_window = Screen()
game_window.tracer(0)
game_window.setup(width=800, height=600)
game_window.bgcolor("black")
game_window.title("Pong")

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

ball = Ball()
score_board = ScoreBoard()
game_window.update()

game_window.onkey(key="Up", fun=r_paddle.up)
game_window.onkey(key="Down", fun=r_paddle.down)
game_window.onkey(key="w", fun=l_paddle.up)
game_window.onkey(key="s", fun=l_paddle.down)
game_window.listen()


def reset_game():
    ball.goto((0, 0))
    l_paddle.goto((-350, 0))
    r_paddle.goto((350, 0))


game_is_on = True
while game_is_on:
    ball.move()
    game_window.update()
    time.sleep(0.05)
    if ball.detect_wall_collision():
        pass
    if ball.detect_collision_with_paddles(left_paddle=l_paddle, right_paddle=r_paddle):
        pass
    paddle = ball.detect_paddle_miss()
    if paddle is not None:
        if paddle == "Right":
            score_board.score_left_paddle += 1
        else:
            score_board.score_right_paddle += 1
        score_board.update_score()
        if score_board.score_left_paddle >= 5 or score_board.score_right_paddle >= 5:
            game_is_on = False
            score_board.game_over()
            print("Game Over")
        else:
            reset_game()

game_window.exitonclick()
