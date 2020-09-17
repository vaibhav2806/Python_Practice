#OPERATOR OVERLOADING 
class student:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    #overloading comparision operator
    def __gt__(self, other):
        r1 = self.a + self.b
        print(r1)
        r2 = other.a + other.b
        print(r2 )
        if r1>r2:
            return True
        else :
            return False
    
    #overloading equality
    def __eq__(self,other):
        r1 = self.a + self.b
        r2 = other.a + other.b
        if (r1 == r2 ):
            return True
        else:
            return False

ob1 = student(44,44)
ob2 = student(88,88)

if ob1 > ob2:
    print("a wins")
elif ob1 == ob2 :
    print("draw")
else:
    print("b wins")