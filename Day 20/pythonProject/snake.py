import turtle as t
STARTING_POSITIONS = [(0,0), (-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = t.Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def add_segment(self):
        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        last_segment_x = self.segments[-1].xcor()
        last_segment_y = self.segments[-1].ycor()
        new_segment.goto(last_segment_x, last_segment_y)
        self.segments.append(new_segment)



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        #if self.head.xcor > 300:
            #self.head.goto(-300, new_y)

    def x_max(self):
        y_cor = self.head.ycor()
        self.head.goto(-300, y_cor)

    def x_min(self):
        y_cor = self.head.ycor()
        self.head.goto(300, y_cor)


    def y_max(self):
        x_cor = self.head.xcor()
        self.head.goto(x_cor, -300)


    def y_min(self):
        x_cor = self.head.xcor()
        self.head.goto(x_cor, 300)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
