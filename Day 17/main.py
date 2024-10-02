# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 22:44:31 2024

@author: Josep
"""

class User():
    def __init__(self, username, id):
        self.name = username
        self.id = id
        self.following = 0
        self.folowers = 0
    
    def Follow(self, user):
        user.folowers += 1
        self.following +=1
    
    def Count(self):
        print(self.following)
        print(self.folowers)
    


user_1 = User("joe", "001")


print(f"hello {user_1.name} your id is {user_1.id}. ")


user_2 = User("bob", "002")

user_3 = User("ann", "002")

user_2.Follow(user_1)

user_1.Count()

user_2.Count()

user_3.Count()