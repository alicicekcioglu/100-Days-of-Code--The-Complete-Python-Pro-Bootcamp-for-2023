import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
timmy.speed(0)
timmy.pensize(1)

turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def draw_spirograph(size_of_gaph):
    for i in range(int(360 / size_of_gaph)):
        timmy.color(random_color())
        timmy.circle(200)
        timmy.setheading(timmy.heading() + size_of_gaph)


draw_spirograph(3)


screen.exitonclick()