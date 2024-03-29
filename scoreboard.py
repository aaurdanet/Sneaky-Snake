from turtle import Turtle

ALIGNMENT = "center"
textSize = 20
FONT = ("courier", textSize, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 268)
        self.score_value = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.update_scoreboard()
        self.shape("blank")
        self.penup()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score_value} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score_value > self.high_score:
            self.high_score = self.score_value
        self.score_value = 0
        record = str(self.high_score)
        with open("data.txt", "w") as data:
            data.write(record)
        self.update_scoreboard()

    def increase_score(self):
        self.score_value += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
