# -*- coding: utf-8 -*-
"""
Ex.3
Biography

"""
Name = input("enter your name: ") #stores the user input
Hometown = input("enter your hometown: ") #stores user input
Age = input("enter your age: ") # before this i used 'int(input())' but that ended up as an error when inputting a string, thats why i removed the input so it can handle both string and integer

bio = { "name": Name,
        "home": Hometown,
        "age": Age}

print ("your",bio["name"],"from",bio["home"],"and",bio["age"],"years old") #prints the keys in the dictionary 
