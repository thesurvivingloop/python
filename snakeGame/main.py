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
        self.m_turtle = Turtle(shape="square")
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

    def forward(self, distance):
        self.m_turtle.forward(distance)

    def heading(self):
        return self.m_turtle.heading()

    def setheading(self, heading):
        self.m_turtle.setheading(heading)


class Snake:
    def __init__(self, initial_length):
        self.snake = []
        self.current_head_direction = 0
        self.new_head_direction = 0
        x = 0
        y = 0
        for _ in range(initial_length):
            new_block = Block()
            new_block.goto(x, y)
            x -= 20
            self.snake.append(new_block)

    def set_direction(self, direction):
        print(f"Inside set_direction. Direction = {direction}")
        if direction == UP and (self.current_head_direction != DOWN and self.current_head_direction != UP):
            self.new_head_direction = direction
            self.snake[0].new_direction = direction
            self.current_head_direction = direction
        elif direction == DOWN and (self.current_head_direction != UP and self.current_head_direction != DOWN):
            self.new_head_direction = direction
            self.snake[0].new_direction = direction
            self.current_head_direction = direction
        elif direction == LEFT and (self.current_head_direction != RIGHT and self.current_head_direction != LEFT):
            self.new_head_direction = direction
            self.snake[0].new_direction = direction
            self.current_head_direction = direction
        elif direction == RIGHT and (self.current_head_direction != LEFT and self.current_head_direction != RIGHT):
            self.new_head_direction = direction
            self.snake[0].new_direction = direction
            self.current_head_direction = direction

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

    def move_one_step(self):
        print("inside move_one_step")
        self.forward(20)

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
        new_block.set_current_direction(last_block.current_direction)
        new_block.set_new_direction(last_block.new_direction)
        # Todo : Set coordinates for the newest created block.


def init_snake():
    game_window.tracer(0)
    snake = Snake(15)
    game_window.update()
    return snake


def onkey_event_handler(key):
    print(f"Inside onkey_event_handle. Key = {key}")
    old_key = key
    if key == "w":
        my_snake.set_direction(UP)
    elif key == "s":
        my_snake.set_direction(DOWN)
    elif key == "a":
        my_snake.set_direction(LEFT)
    elif key == "d":
        my_snake.set_direction(RIGHT)


my_snake = init_snake()

game_window.onkey(key="w", fun=functools.partial(onkey_event_handler, "w"))
game_window.onkey(key="s", fun=functools.partial(onkey_event_handler, "s"))
game_window.onkey(key="a", fun=functools.partial(onkey_event_handler, "a"))
game_window.onkey(key="d", fun=functools.partial(onkey_event_handler, "d"))
game_window.onkey(key="space", fun=my_snake.move_one_step)

game_window.listen()
game_window.exitonclick()
