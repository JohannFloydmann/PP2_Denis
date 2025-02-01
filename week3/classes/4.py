from math import sqrt, pow

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        print(f"x: {self.x}\ny: {self.y}")
        
    def move(self, x, y):
        self.x = x
        self.y = y
        print(f"sucessfully moved to ({self.x}, {self.y})")
        
    def dist(self, other):
        x = other.x - self.x
        y = other.y - self.y
        return sqrt(pow(x, 2) + pow(y, 2))
    
    
first = Point(3, 2)
second = Point(5, 6)
print(first.dist(second))