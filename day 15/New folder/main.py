# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 22:05:33 2024

@author: Josep
"""
MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "milk": 0,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    }


# asks user for their selection
def order():
    order = input("What would you like? (espresso/latte/cappuccino): ")
    cost = {MENU[order]["cost"]}
    #check to see if the machine has enough resources.  if not, it gives a message
    print(f"that will be {cost}")
   
    return(order)

def resource_check(order):
    order_water = MENU[order]["ingredients"]["water"]
    order_milk = MENU[order]["ingredients"]["milk"]
    order_coffee = MENU[order]["ingredients"]["coffee"]
    if resources["water"] < order_water:
        print("Not enough water")
        return(False)
    else:
        return(True)
    if resources["milk"] < order_milk:
        print("Not enough milk")
        return(False)
    else:
        return(True)
    if resources["coffee"] < order_coffee:
        print("Not enough coffee")
        return(False)
    else:
        return(True)


def payment():
    Q_count= int(input("how many Quarters? "))
    D_count= int(input("how many Dimes? "))
    N_count= int(input("how many Nicles? "))
    totalPayment = round((Q_count*0.25+D_count*0.10 +N_count*0.05),2)
    print("you entered {totalPayment}")
    return(totalPayment)
    
def payment_check(totalPayment, cost):
    remainder = 0
    if totalPayment < cost:
        print(f"you entered {totalPayment}, the drink cost {cost}. please enter {cost - totalPayment}")
        remainder = cost - totalPayment
    else:
        print("thank you!")
    return(remainder)

def useMachine():    
    is_true = True
    while is_true:
        orderplaced = order()
        resourceCheck = resource_check(orderplaced)
        if resourceCheck == True:
            pay = payment()
            remainder = payment_check(pay, MENU[orderplaced]["cost"])
            while remainder > 0:
                additionalpay = payment()
                pay = pay + additionalpay
                remainder = payment_check(pay, MENU[orderplaced]["cost"])
            
            print("here is your order")
        order_water = MENU[orderplaced]["ingredients"]["water"]
        order_milk = MENU[orderplaced]["ingredients"]["milk"]
        order_coffee = MENU[orderplaced]["ingredients"]["coffee"]
        
        resources["water"] = resources["water"] - order_water
        resources["milk"] = resources["milk"] - order_milk
        resources["coffee"] = resources["coffee"] - order_coffee
        
        print(resources)
        
        orderagain = input("would you like another order? yes or no")
        if orderagain == "no":
            is_true = False


        
def opperate():
    task = input("would you like to order (1) or check resources (2) ")
    if task == "1": 
        useMachine()
    else:
        print(resources)
                
            
                
        
    
    
    
    
    
    
    
#asks the user how many quarters, nickles and dimes

#if not enough tells them how much more they need and asks them again
#if too much it gives them their change back 

#subtracts the ingredients from the resources 
