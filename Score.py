from turtle import Turtle
import os

X_AXIS = 0
Y_AXIS = 250
DATA_FILE = os.path.join(os.path.dirname(__file__), "data.txt")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        try:
            with open(DATA_FILE) as data:
                self.high_score = int(data.read() or 0)
        except (FileNotFoundError, ValueError):
            self.high_score = 0
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(X_AXIS, Y_AXIS)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High score: {self.high_score}",
            align="center",
            font=("Arial", 24, "normal"),
        )

    def increasesocre(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(DATA_FILE, mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def win(self):
        self.clear()
        self.goto(0, 0)
        self.write("you win", align="center", font=("Arial", 24, "normal"))
