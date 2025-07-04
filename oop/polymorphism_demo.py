import math
class shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the 'area' method.")
class Rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius    
        
        
            