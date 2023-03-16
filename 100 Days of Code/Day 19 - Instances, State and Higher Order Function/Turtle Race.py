from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

screen.title("Turtle Race")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle wil win the race? Enter a color: ")
colors = ["red", "orange", "gold", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index - 1])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)
    new_turtle.pendown()
    new_turtle.pensize(5)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                screen.title(titlestring=f"You won, {winning_turtle} turtle is the winner!")
            else:
                screen.title(titlestring=f"You lost, {winning_turtle} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
