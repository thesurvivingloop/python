from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto((0, 0))
        self.last_x_cor = self.xcor()
        self.last_y_cor = self.ycor()
        self.x_direction = -1
        self.y_direction = -1

    def move(self):
        self.last_x_cor = self.xcor()
        self.last_y_cor = self.ycor()
        self.goto((self.xcor() + (10 * self.x_direction), self.ycor() + (10 * self.y_direction)))

    def detect_wall_collision(self):
        wall_collision = False
        ball_y_cor = self.ycor()
        if ball_y_cor >= 280 or ball_y_cor <= -280:
            print("collided with wall")
            wall_collision = True
            self.y_direction *= -1
        return wall_collision

    def detect_collision_with_paddles(self, left_paddle, right_paddle):
        paddle_collision = False
        if self.distance(left_paddle) < 40 or self.distance(right_paddle) < 40:
            paddle_collision = True
            print("collided with paddle")
            self.x_direction *= -1
        return paddle_collision





