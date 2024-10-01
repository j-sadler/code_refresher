import time
import turtle as t
#import random as rand
from idlelib.macosx import hideTkConsole
from tkinter.ttk import setup_master
from turtledemo.penrose import start
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)




snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#snake.create_snake()


game_is_on = True



def snake_canloop():
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        #detect Collision with food and snake
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.add_score()
            print("nom nom nom")
            snake.add_segment()
        if snake.head.xcor() > 300:
            snake.x_max()
        if snake.head.xcor() < -300:
            snake.x_min()
        if snake.head.ycor() > 300:
            snake.y_max()
        if snake.head.ycor() < -300:
            snake.y_min()

        # Detect colision with tail
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                scoreboard.game_over()
                game_is_on = False

#def no_loop_screen():
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect Collision with food and snake
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        print("nom nom nom")
        snake.add_segment()
    if snake.head.xcor() > 300  or  snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        scoreboard.game_over()
        game_is_on = False

    #Detect colision with tail
    for segment in snake.segments[1:]:
        if  snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False


        #if head collides with tail:
            #triger game over



screen.exitonclick()
