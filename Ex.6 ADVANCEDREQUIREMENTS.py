# -*- coding: utf-8 -*-
"""
ex.6
brute force

@author: Earl
"""
cpass=("pogi")#for storing the password
pas = ""#it acts as a varible for the user input
maxtry= 5#the mmaximum amount of iteration 

tries = 0#is how much tries youve done(will add up in the next code)

while tries <5:#"while" creates a loop while the 'tries<5:'will count the tries till it reaches 5 
    pas=input("enter your password: ")#for getting the paswword
    if pas == cpass:#checking if the statement is correct
        print("correct")#to print if the statement is correct
        break#ends the program if its correct
    else:
        tries+=1#this adds 1 try in the overall tries   
        print("youve tried",tries,"tries")#for printing how much tries youve done
        if tries == 5:#this makes sure that once the amount of tries reaches 5, it will notice you on how much tries youve done
            print("maximum attempts reached")#for printing maximum amount of tries

