# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 23:20:48 2024

@author: Josep
"""

#import turtle
#timmy = turtle.Turtle()

from turtle import Turtle, Screen
timmy = Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color("blue")
timmy.fd(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()



