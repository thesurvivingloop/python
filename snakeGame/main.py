# Snake game sub-problems
# 1. Create a snake style object
# 2. Control the snake to move in any direction
# 3. Determine when the snake hits the boundaries and end game.
# 4. Determine if the snake's head hits it's own body and end game
# 5. Present food in the game at a certain coordinate
# 6. Determine that snake ate food
# 7. Increase length of snake on eating food
# 8. Maintain a scorecard

from turtle import Screen
from snake import *
import time
import functools


def init_snake():
    game_window.tracer(0)
    snake = Snake(5)
    snake.create_food()
    print(f"Snake Initialized. Head position = {snake.snake[0].get_current_position()}. "
          f"Food position = {snake.current_food.get_current_position()}")
    game_window.update()
    return snake


def onkey_event_handler(key):
    print(f"Inside onkey_event_handle. Key = {key}")
    if key == "w":
        my_snake.set_direction(UP)
    elif key == "s":
        my_snake.set_direction(DOWN)
    elif key == "a":
        my_snake.set_direction(LEFT)
    elif key == "d":
        my_snake.set_direction(RIGHT)
    elif key == "space":
        my_snake.move_one_step()
        game_window.update()


game_window = Screen()
game_window.setup(width=600, height=600)
game_window.bgcolor("black")
game_window.title("Snake!!")
my_snake = init_snake()
# while True:
#     time.sleep(0.1)
#     my_snake.move_one_step()
#     my_snake.move_one_step()
#     my_snake.move_one_step()
#     my_snake.snake[0].m_turtle.left(90)

game_window.onkey(key="w", fun=functools.partial(onkey_event_handler, "w"))
game_window.onkey(key="s", fun=functools.partial(onkey_event_handler, "s"))
game_window.onkey(key="a", fun=functools.partial(onkey_event_handler, "a"))
game_window.onkey(key="d", fun=functools.partial(onkey_event_handler, "d"))
game_window.onkey(key="space", fun=functools.partial(onkey_event_handler, "space"))

game_window.listen()
game_window.exitonclick()
