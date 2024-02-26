class Area:
    def __init__(self,pi,r):
        self.pi=pi
        self.r=r
    def display(self):
        self.radius=self.pi*self.r**2
        print(int(self.radius))

a=Area(3.14,5)
a.display()