from turtle import Turtle
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
COORDINATES = [(0, 0), (-20, 0), (-30, 0)]


class Snake:
    def __init__(self):
        self.tims = []
        self.create_snake()
        self.head = self.tims[0]

    def create_snake(self):
        for i in COORDINATES:
            self.add_segment(i)

    def add_segment(self, i):
        tim = Turtle('square')
        tim.penup()
        tim.color('white')
        tim.goto(i)
        self.tims.append(tim)

    def extend(self):
        self.add_segment(self.tims[-1].position())

    def move(self):
        for j in range(len(self.tims) - 1, 0, -1):
            x_axis = self.tims[j - 1].xcor()
            y_axis = self.tims[j - 1].ycor()
            self.tims[j].goto(x_axis, y_axis)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
