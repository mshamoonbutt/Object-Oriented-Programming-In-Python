class SodaCan:
    def __init__(self,height,radius):
        self.height=height
        self.radius=radius
    def getSurfaceArea(self):
        return 2*3.14*self.radius*(self.radius+self.height)
    def getVolume(self):
        return 3.14*(self.radius**2)*self.height

sodacan1=SodaCan(10,15)  
sodacan2=SodaCan(20,33)


print("Surface Area of Soda Can 1:", sodacan1.getSurfaceArea())
print("Surface Area of Soda Can 2:", sodacan2.getSurfaceArea())
print("Volume of Soda Can 1:", sodacan1.getVolume())
print("Volume of Soda Can 2:", sodacan2.getVolume())