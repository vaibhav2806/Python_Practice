class A:
    def __init__(self):
        print("in A init")

    def feature1(self):
        print("working 1")
    
    def feature2(self):
        print("working 2")

class B(A):
    def __init__(self):
        super().__init__()
        print("in B init")

    def feature3(self):
        print("working 3")
    
    def feature4(self):
        print("working 4")

b1 = B()

### when you create object of sub class it wil call init of sub class first but if we use super keyword then it will  first call init of super 
### class then it will call the init of sub class 
