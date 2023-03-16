import turtle
from turtle import Turtle,Screen
import random


timmy = Turtle()
screen = Screen()
timmy.speed(0)
timmy.pensize(8)

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color


angels = range(361)

def moves():
    timmy.forward(40)
    timmy.setheading(random.choice(angels))

for i in range(100):
    timmy.color(random_color())
    moves()

screen.exitonclick()