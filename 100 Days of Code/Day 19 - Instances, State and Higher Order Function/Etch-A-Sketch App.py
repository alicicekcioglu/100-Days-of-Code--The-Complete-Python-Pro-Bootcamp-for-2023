from turtle import Turtle, Screen

tosbaga = Turtle()
screen = Screen()


def clear():
    tosbaga.reset()


def move_forward():
    tosbaga.forward(10)


def move_back():
    tosbaga.back(10)


def counter_clokwise():
    tosbaga.left(10)


def clokwise():
    tosbaga.right(10)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=counter_clokwise)
screen.onkey(key="d", fun=clokwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
