from abc import ABC , abstractmethod

class shape(ABC):
    @abstractmethod
    def print_area(self):
        return 0

class rectangle(shape):
    def __init__(self):
        self.length = 7
        self.breath = 6

    def print_area(self):
        return (self.length * self.breath)

rect1 = rectangle()
print(f"AREA = {rect1.print_area()}")

class square(shape):
    def __init__(self):
        self.side = 4

    def print_area(self):
        return (self.side* self.side)

sq1 = square()

# as we can see that class shape is throwing an error and asking us to define print_area in class square.
# shape class is giving orders to square class to implement print_arae
# once we define print_arae in square then it won't throw any error