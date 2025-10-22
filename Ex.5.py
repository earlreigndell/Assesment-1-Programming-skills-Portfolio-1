# -*- coding: utf-8 -*-
"""
Ex.5

Days of the Month
"""
#a dictionary containing how much days there are in every month
months = {1: 31, 
          2: 28,
          3: 31,
          4: 30,
          5: 31,
          6: 30,
          7: 31,
          8: 31,
          9: 30,
          10: 31,
          11: 30,
          12: 31 
  }

a=int(input("Enter your month number: ")) #stores user input asking for what month they want
if a == 1: #if the selected number is 1
    print("your month is jaunary")
elif a == 2:#if the selected number is 2
    print("your month is February")
elif a == 3:#if the selected number is 3
    print("your month is March")
elif a == 4:#if the selected number is 4
    print("your month is April")
elif a == 5:#if the selected number is 5
    print("your month is May")
elif a == 6:#if the selected number is 6
    print("your month is June")
elif a == 7:#if the selected number is 7
    print("your month is July") 
elif a == 8:#if the selected number is 8
    print("the month is August")
elif a == 9:#if the selected number is 9
    print("the month is September")
elif a == 10:#if the selected number is 10
    print("the month is ctober")
elif a == 11:#if the selected number is 11
    print("the month is November")
elif a == 12:#if the selected number is 12
    print("the month is December")
else: #if the selected number is beyond 12
    print("your month is not valid")
    
print("this month has",months[a],"days") #print the output of a




