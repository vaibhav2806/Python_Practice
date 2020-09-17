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
print(rect1.print_area())

class square(shape):
    def __init__(self):
        self.side = 4

sq1 = square()
