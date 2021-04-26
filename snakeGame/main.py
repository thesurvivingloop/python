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


def init_snake():
    game_window.tracer(0)
    snake = Snake(5)
    snake.create_food()
    print(f"Snake Initialized. Head position = {snake.snake[0].get_current_position()}. "
          f"Food position = {snake.current_food.get_current_position()}")
    game_window.update()
    return snake


def onkey_up():
    print("Up")
    my_snake.set_direction(UP)


def onkey_down():
    print("Down")
    my_snake.set_direction(DOWN)


def onkey_left():
    print("Left")
    my_snake.set_direction(LEFT)


def onkey_right():
    print("Right")
    my_snake.set_direction(RIGHT)


UP_KEY = "Up"
DOWN_KEY = "Down"
RIGHT_KEY = "Right"
LEFT_KEY = "Left"

game_window = Screen()
game_window.setup(width=600, height=600)
game_window.bgcolor("black")
game_window.title("Snake!!")
my_snake = init_snake()

game_window.listen()
game_window.onkey(key=UP_KEY, fun=onkey_up)
game_window.onkey(key=DOWN_KEY, fun=onkey_down)
game_window.onkey(key=RIGHT_KEY, fun=onkey_right)
game_window.onkey(key=LEFT_KEY, fun=onkey_left)

while True:
    time.sleep(0.1)
    my_snake.move_one_step()
    game_window.update()

game_window.exitonclick()






