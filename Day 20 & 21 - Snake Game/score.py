from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score {self.score} High Score {self.high_score}",align= ALIGNMENT, font=FONT)
    #
    # def show_score(self):
    #     self.write(arg=f"Score: {str(self.score)}", move=False, align=ALIGNMENT, font=FONT)

    def calculate_score(self):
        self.clear()
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game Over!", move=False, align=ALIGNMENT, font=FONT)

