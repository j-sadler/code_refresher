from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.go_to_start()



    def is_at_finish_line(self):
        if self.ycor() > 250:
            print("One point!")
            return True

    def go_to_start(self):
        self.goto(0, -230)


    def move_up(self):
        new_y = self.ycor() +10
        x_cor = self.xcor()
        self.goto(x_cor, new_y)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.back(20)


