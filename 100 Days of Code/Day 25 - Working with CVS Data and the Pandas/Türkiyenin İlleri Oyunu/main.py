import turtle
import pandas

screen = turtle.Screen()
screen.title("İl Tahmin Etme")
image = "6e258d2d2790db9adf0961bc3a12d45a.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=1400, height=800)

data = pandas.read_csv("iller.csv", encoding="utf-8-sig")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 81:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/81 States Correct",
                                    prompt="What's another state's name?").title()
    print(answer_state)
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(float(state_data.x), float(state_data.y))
        t.write(state_data.state.item(), align="center", font=("Arial", 11, "bold"))