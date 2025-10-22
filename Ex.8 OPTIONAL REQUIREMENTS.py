# -*- coding: utf-8 -*-
"""
Ex.8
Simple Search

"""
#crates a dictionary for storing the names 
names = {
        "Jake": 1,
        "Zac": 2,
        "Ian": 3,
        "Ron": 4,
        "Sam": 5,
        "Dave": 6 }

#a asks for the name
a = input("enter the name your looking for: ")

#checks if the name is in the dictionary
if a in names:
    print (f"{a} was in found")
#prints if not found
else:
    print (f"{a} was not found")