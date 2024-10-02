# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 22:35:29 2024

@author: Josep
"""

starting_dictionary = {
    "a": 9,
    "b": 8,
}

final_dictionary = starting_dictionary["c"] = 7

print(final_dictionary)
print(starting_dictionary)

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

dict[1] = 4