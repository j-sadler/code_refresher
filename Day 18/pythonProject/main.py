import turtle as t
import random

tim = t.Turtle()


def line_dash():
    for _ in range(15):
        tim.forward(10)
        tim.penup()

        tim.forward(10)
        tim.pendown()


def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides
        tim.forward(100)
        tim.right(angle)


direction = [0, 90, 180, 270]
t.colormode(255)

# tim.pensize(15)
# tim.speed( "fastest")

def multi_shapes(max_sides):
    for shape_sides_n in range(3, max_sides):
        draw_shape(shape_sides_n)


def random_walk(step_count):
    for _ in range(step_count):
        tim.forward(30)
        tim.color(random_color())
        tim.right(int(random.choice(direction)))
    screen= t.Screen()
    screen.exitonclick()



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_choice = (r, g, b)
    return color_choice

def random_walk_h(step_count):
    for _ in range(step_count):
        tim.forward(30)
        tim.color(random_color())
        tim.right(int(random.choice(direction)))
    screen= t.Screen()
    screen.exitonclick()


random_walk_h(50)

"""      
for _ in range(40):
    tim.forward(30)
    tim.right(int(random.choice(direction)))
"""

