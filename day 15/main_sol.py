# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:06:18 2024

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


is_on = True

profit = 0

def is_resource_sufficient(order_ingredients):
    """ returns True when the order can be made """
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"there is not enough {item} in the machine.")
            return False
    return True

def process_coins():
    """ returnes the total calculated from coins inserted"""
    print("please insert coints")
    Q_count= int(input("how many Quarters? "))
    D_count= int(input("how many Dimes? "))
    N_count= int(input("how many Nicles? "))
    total = round((Q_count*0.25+D_count*0.10 +N_count*0.05),2)
    return total

def is_payment_sufficient(payment, price):
    """ return True if accepted and False if insufficient"""
    if payment >= price:
        change = round(payment - price, 2)
        print(f"here is ${change} in change.")
        global profit
        profit += price
        return True
    else:
        print("not enough money")
        return False
    

def make_coffee(drink_name):
    for item in drink_name["ingredients"]:
        #global resources
        resources[item] -= drink_name["ingredients"][item]
        print("here is your {drink_name}")
        
    
while is_on:
    choice = input("What would you like?(espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(resources)
        print(profit)
        print(f"the machine has {resources} remaining and {profit} money")
    else:
         drink = MENU[choice]
         print(drink)
         if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_payment_sufficient(payment, drink["cost"]):
                make_coffee(drink)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    