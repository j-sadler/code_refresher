from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()


        self.shape("square")

        self.penup()
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.speed("fastest")
        if side == "l":
            self.goto(-350,0)
        elif side == "r":
            self.goto(350,0)

        self.color("white")



    def up(self):
        x_cor = self.xcor()
        new_y = self.ycor() + 20
        self.goto(x_cor, new_y)

    def down(self):
        x_cor = self.xcor()
        new_y = self.ycor() - 20
        self.goto(x_cor, new_y)








