# Snake game sub-problems
# 1. Create a snake style object
# 2. Control the snake to move in any direction
# 3. Determine when the snake hits the boundaries and end game.
# 4. Determine if the snake's head hits it's own body and end game
# 5. Present food in the game at a certain coordinate
# 6. Determine that snake ate food
# 7. Increase length of snake on eating food
# 8. Maintain a scorecard

from turtle import Turtle, Screen
import random
import time
import functools

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

game_window = Screen()
game_window.setup(width=600, height=600)
game_window.bgcolor("black")
game_window.title("Snake!!")


class Block:
    def __init__(self):
        self.m_turtle = Turtle(shape="circle")
        self.m_turtle.speed("slow")
        self.m_turtle.color("white")
        self.m_turtle.penup()
        self.current_direction = self.m_turtle.heading()
        self.new_direction = self.current_direction

    def set_current_direction(self, direction):
        self.current_direction = direction
        self.m_turtle.setheading(direction)

    def set_new_direction(self, direction):
        self.new_direction = direction

    def goto(self, x, y):
        self.m_turtle.goto(x, y)

    def goto_position(self, pos):
        x_cord = pos[0]
        y_cord = pos[1]
        self.m_turtle.goto(x_cord, y_cord)

    def forward(self, distance):
        self.m_turtle.forward(distance)

    def heading(self):
        return self.m_turtle.heading()

    def setheading(self, heading):
        self.m_turtle.setheading(heading)

    def get_current_position(self):
        x = round(self.m_turtle.xcor())
        y = round(self.m_turtle.ycor())
        pos = (x, y)
        return pos


class Snake:
    def __init__(self, initial_length):
        self.snake = []
        self.current_head_direction = 0
        self.new_head_direction = 0
        self.current_food = None
        x = 0
        y = 0
        for _ in range(initial_length):
            new_block = Block()
            new_block.goto(x, y)
            x -= 20
            self.snake.append(new_block)
        self.last_tail_position_before_move = self.snake[-1].get_current_position()

    def set_direction(self, direction):
        print(f"Inside set_direction. Direction = {direction}")
        if direction == UP and (self.current_head_direction != DOWN and self.current_head_direction != UP):
            self.new_head_direction = direction
            self.snake[0].new_direction = direction
            self.current_head_direction = direction
            self.snake[0].setheading(direction)
        elif direction == DOWN and (self.current_head_direction != UP and self.current_head_direction != DOWN):
            self.new_head_direction = direction
            self.snake[0].new_direction = direction
            self.current_head_direction = direction
            self.snake[0].setheading(direction)
        elif direction == LEFT and (self.current_head_direction != RIGHT and self.current_head_direction != LEFT):
            self.new_head_direction = direction
            self.snake[0].new_direction = direction
            self.current_head_direction = direction
            self.snake[0].setheading(direction)
        elif direction == RIGHT and (self.current_head_direction != LEFT and self.current_head_direction != RIGHT):
            self.new_head_direction = direction
            self.snake[0].new_direction = direction
            self.current_head_direction = direction
            self.snake[0].setheading(direction)

    def forward(self, step_size):
        previous_block = None
        for block in self.snake:
            if previous_block is None:
                if block.new_direction != block.current_direction:
                    block.set_current_direction(block.new_direction)
                block.forward(step_size)
                previous_block = block
            else:
                if block.new_direction != block.current_direction:
                    block.set_current_direction(block.new_direction)
                    block.forward(step_size)
                    if block.new_direction != previous_block.current_direction:
                        block.new_direction = previous_block.current_direction
                elif block.current_direction != previous_block.current_direction:
                    if previous_block.current_direction == previous_block.new_direction:
                        block.forward(step_size)
                        block.new_direction = previous_block.current_direction
                    else:
                        block.new_direction = previous_block.current_direction
                        block.forward(step_size)
                else:
                    block.forward(step_size)
                previous_block = block
        game_window.update()
        # self.dump_snake_state()

    def forward_new(self, step_size):
        print("inside forward_new")
        for i in reversed(range(1, len(self.snake))):
            previous_block_position = self.snake[i-1].get_current_position()
            self.snake[i].goto_position(previous_block_position)
        self.snake[0].forward(step_size)
        game_window.update()

    def move_one_step(self):
        print("inside move_one_step")
        # self.forward(20)
        self.last_tail_position_before_move = self.snake[-1].get_current_position()
        print(f"last_tail_position_before_move = {self.last_tail_position_before_move}")
        self.forward_new(20)
        print(f"snake_head_position = {self.snake[0].get_current_position()}")
        print(f"food_position = {self.current_food.get_current_position()}")
        if self.snake[0].get_current_position() == self.current_food.get_current_position():
            self.create_food()
            self.add_one_block()
            print("food eaten")

    def dump_snake_state(self):
        print("------\n")
        print(f"current_head_direction = {self.current_head_direction}")
        print(f"first_block_direction = {self.snake[0].m_turtle.heading()}")

        for i in range(0, len(self.snake)):
            print(f"----- block [{i}] -----")
            print(f"current_direction = {self.snake[i].current_direction}")
            print(f"new_direction = {self.snake[i].new_direction}")
            print(f"heading = {self.snake[i].m_turtle.heading()}")
        print("------\n")

    def add_one_block(self):
        snake_length = len(self.snake)
        last_block = self.snake[snake_length - 1]
        new_block = Block()
        new_block.goto_position(self.last_tail_position_before_move)
        self.snake.append(new_block)
        new_block.set_current_direction(last_block.current_direction)
        new_block.set_new_direction(last_block.new_direction)

    def create_food(self):
        if self.current_food is not None:
            old_food = self.current_food
            old_food.m_turtle.clear()
            old_food.m_turtle.hideturtle()
            del old_food
            game_window.update()
        x_cord = random.randint(0, 280)
        y_cord = random.randint(0, 280)
        x_remainder = x_cord % 20
        y_remainder = y_cord % 20
        x_cord -= x_remainder
        y_cord -= y_remainder
        print(f"food coordinates {x_cord,y_cord}")
        food = Block()
        food.goto(x_cord, y_cord)
        self.current_food = food
        game_window.update()


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
game_window.onkey(key="space", fun=my_snake.move_one_step)

game_window.listen()
game_window.exitonclick()
