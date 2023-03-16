from turtle import Turtle, Screen
"""
turtle.listen(xdummy=None, ydummy=None)
Set focus on TurtleScreen (in order to collect key-events). Dummy arguments are provided in order to be able to pass 
listen() to the onclick method.

turtle.onkey(fun, key)
turtle.onkeyrelease(fun, key)

Parameters: fun – a function with no arguments or None
            key – a string: key (e.g. “a”) or key-symbol (e.g. “space”)
"""


tosbaga = Turtle()
screen = Screen()

def move_forward():
    tosbaga.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()