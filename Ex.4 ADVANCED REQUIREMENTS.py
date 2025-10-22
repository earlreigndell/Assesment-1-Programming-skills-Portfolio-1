"""
primitive quiz 
ex 4.
"""
no1=(input("What is the capital of france? ")) #no1 is the variable for storing the user input
print("") #this is for spacing only
if no1.lower()=="paris": #the command .lower can convert all uppercase characters within a string to their lowercase equivalents. and the word ok next == means it should be the answer
   print("your answer is correct") #for displaying the "correct" answer
else: #else command is used for if the answer needed is incorrect
    print("your answer is wrong") #for displaying the "incorrect" answer 

print("") #for spacing

no2=(input('Now,try to answer these other countries capitals'))#for storing user input
print("")
if no2.lower()=="ok":#same as the first one, now the answer is 'ok'
   print("okay here we go")#prints if the answer given is ok
   
else:
    print("aww too bad, you have to")#this will print if the answer given is not "ok"
    
print("") #for spacing


"""
the part below would be the 10 other europian countries 
"""


con1=(input("What is the capital of spain? "))#for stroing user input

if con1.lower()=="madrid":# makes it so the word 'madrid' in any capital order the right answer
   print("wow nice, your answer is correct") #prints if the the answer is 'madrid'
else:
    print("your answer is wrong, try again later") #prints if the answer is not 'madrid'
    
print("") # for spacing
    
con2=(input("What is the capital of Sweden? "))#for storing user input

if con2.lower()=="stockholm":# makes it so the word 'stockholm' in any capital order the right answer
   print("your in a roll, keep going") #prints if the answer is 'stockholm'
else:
    print("Incorrect, try again later") #prints if the aswer is not 'stockholm'
    
print("")
    
con3=(input("What is the capital of Finland? "))#for storing user input

if con3.lower()=="helsinki":# makes it so the word 'helsinki' in any capital order the right answer
   print("wow how did you get that, keep it going") #prints if the answer is 'helsinki'
else:
    print("nice try, even i wouldnt get that, try again later") #prints if the answer is not 'helsinki'

print("") #for spacing

con4=(input("What is the capital of norway? "))#for storing user input

if con4.lower()=="oslo":# makes it so the word 'oslo' in any capital order the right answer
   print("Niceee, your on a streak") #prints is the answer is 'oslo'
else:
    print("thats okay, try again") #prints if the answer is not 'oslo'
    
print("") #for spacing

con5=(input("What is the capital of poland? "))#for storing user input

if con5.lower()=="warsaw":# makes it so the word 'warsaw' in any capital order the right answer
   print("No wayy you got that, nicee") #prints if the answer is 'warsaw'
else:
    print("i expected this, your answer is wrong") #prints if the answer is not 'warsaw'

print("") #for spacing

con6=(input("What is the capital of italy? "))#for storing user input

if con6.lower()=="rome":# makes it so the word 'rome' in any capital order the right answer
   print("As expected, this one was easy")  #prints if the answer is 'rome'  
else:
    print("really??, try again") #prints if the answer is not 'rome'
   
print("") #for spacing

con7=(input("What is the capital of ukrain? "))#for storing user input

if con7.lower()=="kyiv":# makes it so the word 'kyiv' in any capital order the right answer
   print("how did you get that, like actually, nice one tho") #prints if the answer is 'kyiv'
else:
    print("aww thats okay, i would be more surprised if you got it right") #prints if the answer is not 'kyiv'

print("") #for spacing

con8=(input("What is the capital of russia? "))#for storing user input

if con8.lower()=="moscow":# makes it so the word 'moscow' in any capital order the right answer
   print("yesss, correction tape") #prints if the answer is 'moscow'
else:
    print("nice try, you were almost there") #prints if the answer is not 'moscow'
    
print("") #for spacing

con9=(input("What is the capital of belgium? "))#for storing user input

if con9.lower()=="brussels":# makes it so the word 'brussels' in any capital order the right answer
   print("nice, you searched this up didnt you, eitherway your almost done")  #prints if the answe is 'brussels'  
else:
    print("incorrect, nice guess tho") #prints if the answer is not 'brussels'
    
print("") #for spacing

con10=(input("LAST QUESTION, What is the capital of moldova? "))#for storing user input

if con10.lower()=="Chișinău": # makes it so the word 'Chișinău' in any capital order the right answer
   print("Congratulations, if you got this correct, you derve a medal, actually") #prints if the answer is 'Chișinău'
else:
    print("dont frown, nice try") #prints if the answer is not 'Chișinău'



