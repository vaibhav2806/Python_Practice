a = int(input("Enter first number: \n "))
b = int(input("Enter second number: \n "))

maxNum = max (a , b)

while(True):
    if (maxNum % a == 0) and (maxNum % b == 0):
        break
    maxNum += 1
print (f"L.C.M of {a} and {b} is {maxNum}")