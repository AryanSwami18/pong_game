from turtle import Turtle

SCORE_A = 0
SCORE_B = 0


def score_update_b():
    global SCORE_B
    SCORE_B += 1


def score_update_a():
    global SCORE_A
    SCORE_A += 1


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)

    def score_update_a(self):
        global SCORE_A
        SCORE_A += 1
        self.clear()
        self.write(f"Player A:{SCORE_A} | Player B:{SCORE_B}", align="center", font=("arial", 15, "normal"))

    def score_update_b(self):
        global SCORE_B
        SCORE_B += 1
        self.clear()
        self.write(f"Player A:{SCORE_A} | Player B:{SCORE_B}", align="center", font=("arial", 15, "normal"))
