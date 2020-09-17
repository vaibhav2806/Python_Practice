#operator overloading

class student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self,other):
        return self.m1 + other.m1 , self.m2 + other.m2

    def __str__(self):
        return self.m1 , self.m2

ob1 = student(56,65)
ob2 = student(75,25)
ob3 = ob1 + ob2 
print(ob3)