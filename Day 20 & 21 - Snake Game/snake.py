from turtle import Turtle

STARTING_POSTION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

"""
hızı ve pozisyonu yukarı alıyoruz ve büyük harfle yazıyoruz ki ilerde hızı ve ya pozisyonu değiştirmek istersek 
fonkiyonlarla uğraşmadan buradaki değerleri değiştirelim.
"""


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for i in STARTING_POSTION:
            self.add_segment(i)

    def add_segment(self, i):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.shapesize(1, 1)
        new_segment.goto(i)
        self.segment.append(new_segment)

    def reset(self):
        for i in self.segment:
            i.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def extend(self):
        # add new segment to the snake.
        self.add_segment(self.segment[-1].position())

    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[i - 1].xcor()
            new_y = self.segment[i - 1].ycor()
            self.segment[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
