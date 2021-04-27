from block import Block
from food import Food
import random

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


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
        # self.dump_snake_state()

    def forward_new(self, step_size):
        print("inside forward_new")
        for i in reversed(range(1, len(self.snake))):
            previous_block_position = self.snake[i-1].get_current_position()
            self.snake[i].goto_position(previous_block_position)
        self.snake[0].forward(step_size)

    def move_one_step(self):
        print("inside move_one_step")
        # self.forward(20)
        ate_food = False
        self.last_tail_position_before_move = self.snake[-1].get_current_position()
        print(f"last_tail_position_before_move = {self.last_tail_position_before_move}")
        self.forward_new(20)
        print(f"snake_head_position = {self.snake[0].get_current_position()}")
        print(f"food_position = {self.current_food.pos()}")
        if self.snake[0].get_current_position() == self.current_food.pos():
            ate_food = True
            self.create_food()
            self.add_one_block()
            print("food eaten")
        return ate_food

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
            old_food.clear()
            old_food.hideturtle()
            del old_food
        food = Food()
        print(f"food coordinates = {food.pos()}")
        self.current_food = food
