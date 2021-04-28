from turtle import Screen
from paddle import Paddle
from ball import Ball
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

game_window.onkey(key="Up", fun=r_paddle.up)
game_window.onkey(key="Down", fun=r_paddle.down)
game_window.onkey(key="w", fun=l_paddle.up)
game_window.onkey(key="s", fun=l_paddle.down)

game_window.listen()

game_is_on = True
while game_is_on:
    ball.move()
    game_window.update()
    time.sleep(0.1)
    if ball.detect_wall_collision():
        pass
    if ball.detect_collision_with_paddles(left_paddle=l_paddle, right_paddle=r_paddle):
        pass

game_window.exitonclick()
