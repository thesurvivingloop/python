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
from food import Food
from scoreboard import ScoreBoard
import time


def init_snake():
    game_window.tracer(0)
    snake = Snake(5)
    snake.create_food()
    print(f"Snake Initialized. Head position = {snake.snake[0].get_current_position()}. "
          f"Food position = {snake.current_food.pos()}")
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
# food = Food()
score_board = ScoreBoard()

game_window.listen()
game_window.onkey(key=UP_KEY, fun=onkey_up)
game_window.onkey(key=DOWN_KEY, fun=onkey_down)
game_window.onkey(key=RIGHT_KEY, fun=onkey_right)
game_window.onkey(key=LEFT_KEY, fun=onkey_left)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    food_eaten = my_snake.move_one_step()
    if food_eaten:
        score_board.update_score()

    snake_head = my_snake.snake[0].m_turtle
    if snake_head.xcor() > 280  or snake_head.xcor() < -280 or snake_head.ycor() > 280 or snake_head.ycor() < -280:
        game_is_on = False
        score_board.game_over()

    for i in range(0, len(my_snake.snake)):
        if i > 0 and snake_head.distance(my_snake.snake[i].m_turtle) < 10:
            game_is_on = False
            score_board.game_over()

    game_window.update()

game_window.exitonclick()






