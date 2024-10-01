from turtle import Turtle
import random
COLORS = ["red", "green", "blue" , "purple", "yellow"]
STARTING_MOVE_DISTANCE = 10
LEVEL_UP = 10

class CarManager:
    def __init__(self):

        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def add_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1 :
            new_car = Turtle("square")

            new_car.color(random.choice(COLORS))
            new_car.shapesize(1,2)
            new_car.penup()
            y_start = random.randint(-200, 240)
            new_car.goto(200,y_start)
            new_car.setheading(180)
            self.car_list.append(new_car)



    def move_car(self):
        for car in self.car_list:
            car.forward(STARTING_MOVE_DISTANCE)
        #new_x = self.xcor() + 5
        #ycor = self.ycor
        #self.goto(new_x, ycor)

    def level_up_speed(self):
        self.car_speed += LEVEL_UP

    def reset(self):
        self.car_speed = STARTING_MOVE_DISTANCE





