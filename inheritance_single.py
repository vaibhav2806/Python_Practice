class A:
    def feature1(self):
        print("feature 1 workng")
    def feature2(self):
        print("feature 2 working")

class B(A):
    def feature3(self):
        print("feature 3 working")
    def feature4(self):
        print("feature 4 working")

z = B()
z.feature4

