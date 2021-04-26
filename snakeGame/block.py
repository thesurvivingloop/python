from turtle import Turtle


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
