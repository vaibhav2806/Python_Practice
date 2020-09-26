# METHOD OVERRIDING - Over riding means having 2 methods with same name and parameters 1 of the method is in the parent class &the other is in child class.

class A:
    def show(self):
        print("in A show")

# Here we are overriding the show method of class A.
class B:
    def show(self):
        print("in B show")

a1 = B()
a1.show()