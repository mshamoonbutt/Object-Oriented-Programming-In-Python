class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.142
        
    def Area(self):
        return (self.pi * self.radius ** 2)
    
    def Perimeter(self):   
        return (2 * self.pi * self.radius)
    
circle1 = Circle(4)
circle2 = Circle(5)
    
radius = int(input("Enter Radius: "))
circle3 = Circle(radius)
     
    
print("Area of circle 1:",circle1.Area())
print()