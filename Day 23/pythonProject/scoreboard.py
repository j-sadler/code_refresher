from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(-100, 220)
        self.write(f"Scrore: {self.score}",  align = ALIGNMENT, font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Scrore: {self.score}", align=ALIGNMENT, font=FONT)