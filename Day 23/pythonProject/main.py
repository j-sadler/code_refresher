import random
from turtle import  Screen
import time
from player import Player
from car_manager import  CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(500, 500)
screen.tracer(0)





player = Player()

cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "w")
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.go_down, "Down")



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.add_car()
    cars.move_car()



    for car in cars.car_list:
        if car.distance(player) < 20:
            game_is_on = False
            print("Game Over!")

    # Detect whe Player has
    if player.is_at_finish_line() == True:
        print("One point!")
        scoreboard.add_score()
        player.go_to_start()
        cars.level_up_speed()
        print(cars.car_speed)


    screen.update()



