# DUCK TYPING : emphasises on what the object can really do 

class bird:
    def fly(self):
        print("fly with wings")

class airplane:
    def fly(self):
        print("fly with fuel")

class fish:
    def fly(self):
        print("fish do not fly")

    def swim(self):
        print("swim in sea")
    

for obj in bird() , airplane() , fish():
    obj.fly()
    