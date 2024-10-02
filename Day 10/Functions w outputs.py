# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 23:59:58 2024

@author: Josep
"""
last_n = input("what is you last name: ")
first_n = input("what is you first name: ")


def formate_name(f_name, l_name):
    T_f_name = f_name.title()
    T_l_name = l_name.title()
    print(f"Your name is {T_f_name} {T_l_name}")
          
          
formate_name(f_name = first_n, l_name = last_n)
    
