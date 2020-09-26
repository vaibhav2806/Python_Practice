# METHOD OVERLOADING - Overloading occurs when 2 or more methods in 1 class have the same name but different parameters
# method overloading isn't directly supported by python

def products(self, a = None, b = None, c = None):
    s = 0
    if (a != None and b != None and c != None):
        s = a+b+c

    elif (a != None and b != None):
        s = a+b

    else:
        s = a
    return s
     
print(products(56,65,89))
print(products(25,52))
print(products(25))
