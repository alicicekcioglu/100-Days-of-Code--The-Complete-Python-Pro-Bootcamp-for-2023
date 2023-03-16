import random
from turtle import Turtle, Screen
import turtle
timmy = Turtle()
screen = Screen()
timmy.speed(0)
timmy.hideturtle()
timmy.pensize(1)
turtle.colormode(255)

color_list = [(245, 243, 238), (247, 242, 244), (240, 245, 241), (202, 164, 109), (238, 240, 245), (150, 75, 49),
              (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71),
              (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158),
              (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20),
              (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

def random_color():
    random_color = random.choice(color_list)
    return random_color


def forward_ten():
    for i in range(10):
        timmy.color((random_color()))
        timmy.dot(20)
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()

def move_start():
    timmy.rt(270)
    timmy.penup()
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.left(180)



for i in range(10):
    forward_ten()
    move_start()


screen.exitonclick()