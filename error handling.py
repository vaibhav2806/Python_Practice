# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

numA = int(input("enter a number:"))
numB = int(input("enter a number:"))
numC = int(input("enter a number:"))

try:
    if numA<numB and numA<numC:
        print("numA is the samallest number"

    elif numB<numA and numB<numC:
        print("numB is the smallest number")
    
    else:
        print("numC is the smallest number")

except:
    print('x'*50)
    print("There is an error")
    print('x'*50)

else:
    avg = (numA + numB + numC) /3
    print("avg of all numbers is: " + avg)
    

    
    
    