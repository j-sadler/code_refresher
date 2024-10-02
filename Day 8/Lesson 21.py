# -*- coding: utf-8 -*-
"""
Created on Thu Feb 29 01:09:27 2024

@author: Josep
"""

#make function that takes a number and tells you if it is prime

def is_prime(number):
    test = True
    for i in range(2, number):
        if number % i == 0:
            test = False
    print(f"{number} is {test}")
    
n = int(input("what number would you like to test "))
is_prime(number = n)