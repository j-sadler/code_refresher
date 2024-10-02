# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 23:10:07 2024

@author: Josep
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 21:30:41 2024

@author: Josep
"""

#Add
def add(n1, n2):
    return n1 + n2



#Subtract
def subtract(n1, n2):
    return n1 - n2


#Mutl
def multiply(n1, n2):
    return n1 * n2


#divide
def divide(n1, n2):
    return n1 / n2


operations = { 
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
    }

num1 = int(input("what is the 1st number? "))
num2 = int(input("what is the 2nd number? "))
for symbol in operations:
    print(symbol)
op = input("what is the operation? ")

op_selected = operations[op]



Continue_Calc = True
output = op_selected(num1, num2)
print(f"{num1} {op} {num2} = {output}")

cont = input("would you like to continue? y for yes, n for no: ")
    
if cont == "y":
    Continue_Calc = True
else:
    Continue_Calc = False

while Continue_Calc == True:
    new_num = int(input("what is the new number? "))
    op = input("what is the operation? ")
    op_selected = operations[op]
    new_output = op_selected(output, new_num)
    print(f"{output} {op} {new_num} = {new_output}")
    output = new_output
    cont = input("would you like to continue? y for yes, n for no: ")
    
    if cont == "y":
        Continue_Calc = True
    else:
        Continue_Calc = False
    