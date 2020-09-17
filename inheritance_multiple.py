# Method resolution order
class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("working 1")
    
    def feature2(self):
        print("working 2")

class B:
    def __init__(self):
        print("in B init")
    def feature3(self):
        print("working 3")
    
    def feature4(self):
        print("working 4")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C init")

    def feature5(self):
        print("working 5")
    
    def feature6(self):
        print("working 6")

z = C()
z.feature3


