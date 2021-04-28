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
        collision_detected = False
        ball_y_cor = self.ycor()
        ball_x_cor = self.xcor()
        if ball_y_cor >= 280:
            print("collided with upper wall")
            collision_detected = True
            if ball_x_cor > self.last_x_cor:
                print("ball is traveling up and right")
                self.y_direction *= -1
            else:
                print("ball is traveling up and left")
                self.y_direction *= -1
        elif ball_y_cor <= -280:
            print("collided with lower wall")
            collision_detected = True
            if ball_x_cor > self.last_x_cor:
                print("ball is traveling down and right")
                self.y_direction = 1
            else:
                print("ball is traveling left and down")
                self.y_direction = 1
        return collision_detected

    def detect_collision_with_paddles(self, left_paddle, right_paddle):
        paddle_collision = False
        ball_xcor = self.xcor()
        ball_ycor = self.ycor()
        if self.distance(left_paddle) < 40:
            paddle_collision = True
            print("collided with left paddle")
            if ball_ycor > self.last_y_cor:
                print("moving up and left")
                self.x_direction *= -1
            else:
                print("moving down and left")
                self.x_direction *= -1
        elif self.distance(right_paddle) < 40:
            paddle_collision = True
            print("collided with right paddle")
            if ball_ycor > self.last_y_cor:
                print("moving up and right")
                self.x_direction *= -1
            else:
                print("moving down and right")
                self.x_direction *= -1
        return paddle_collision




