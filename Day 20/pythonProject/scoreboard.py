import turtle
from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        #self.shapesize(0)
        self.score = 0

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)


        self.write(f"score is {self.score}", align = ALIGNMENT, font=FONT)

    def add_score(self):
        self.clear()
        self.score +=1
        self.write(f"score is {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


