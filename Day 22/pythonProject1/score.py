from turtle import Turtle
FONT = ('Arial', 24, 'normal')
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self, side):
        super().__init__()
        self.score = 0

        self.color("white")
        self.hideturtle()
        self.penup()
        if side == "l":
            self.goto(-200,260)
        elif side == "r":
            self.goto(200,260)


        self.write(self.score, align= ALIGNMENT, font=FONT)


    def add_point(self):
        self.score +=1
        self.clear()

        self.write(self.score, align=ALIGNMENT, font=FONT)
