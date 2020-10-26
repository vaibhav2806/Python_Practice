# -*- coding: utf-8 -*-

import re                                    #regex library
print("MY CLACULATOR")
print("Type 'quit' to exit")                 #to exit from calculator
previous = 0                                 #to hold the previous value  
run = True                                   #calcultor turned on

def perform_math():                          #math function to perform problems 
    global run                               #used global to access the run variable which is outside the fucntion
    global previous 
    
    if previous == 0:                        #if no task is done on calculator yet
        equation = input("Enter Equation: ") #we will give input to calculator
    else: #if prv is not equal tp 0 then prv holds some value an we will use it as input and perform the task stated
        equation = input(str(previous))
        
    if equation == 'quit':                   #to turn off the calculator
        print("Goodbye")
        run = False
    else:                                    #to perform task on calculator
        equation = re.sub('[a-zA-Z,.\:_()<>;" "]' , '', equation) #this helps to take numbers and arithmatic operations as input 
        if previous == 0:
            previous = eval(equation)        #eval helps us to do arithmatic operations it is a built in function 
        else:
            previous =eval(str(previous) + equation)

        
while run:                                   #while the calculator is on we will perform math function
    perform_math()
    

