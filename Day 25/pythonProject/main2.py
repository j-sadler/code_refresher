# import turtle
#
# screen = turtle.Screen()
# screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
#
#
# turtle.shape(image)
#
# answer_state = screen.textinput(title = "guess the state", prompt = "what is another States name")
# print(answer_state)
#
#
# screen.exitonclick()
import random
from numpy.random import random

num = [1, 2, 3]

new_list = []

new_list8 = [i * 4   for i in num]

print(new_list8)

#names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
#student_score = {new_key:new_value for item in list}

#student_score = {student:random.randint(0, 100) for student in names}

#new_dict = {new_key:new_value for (key, value) in dict.items() if test}

#passed_students = {student:score for student in student_score.items() if score > 70}

#dict from dataframe
#dict = {new_key:New_value for (index, row) in df.iterrows()}
