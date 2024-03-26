from turtle import Turtle

ALIGNMENT = "center"
textSize = 24
FONT = ("courier", textSize, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 268)
        self.score_value = 0
        self.color("white")
        self.update_scoreboard()
        self.shape("blank")
        self.penup()

    def update_scoreboard(self):
        self.write(f"Score: {self.score_value}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score_value += 1
        self.clear()
        self.update_scoreboard()
