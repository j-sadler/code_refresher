from turtle import Turtle, Screen
import paddle as p
from ball import Ball
import time
from score import Score
import random

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
paddle_l = p.Paddle("l")
paddle_r = p.Paddle("r")
ball = Ball()
score_l = Score("l")
score_r = Score("r")

screen.listen()

screen.onkeypress(paddle_r.up, "Up")
screen.onkeypress(paddle_r.down, "Down")
screen.onkeypress(paddle_l.up, "w")
screen.onkeypress(paddle_l.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()
    if ball.distance(paddle_l) < 50 and ball.xcor() < -330:
        ball.hit()
    if ball.distance(paddle_r) < 50 and ball.xcor() > 330:
        ball.hit()
    if ball.xcor() < -350:
        ball.reset()
        score_r.add_point()

    if ball.xcor()  > 350:
        ball.reset()
        score_l.add_point()

screen.exitonclick()