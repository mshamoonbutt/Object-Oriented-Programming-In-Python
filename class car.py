class Car:
    def myHybrid(self,effciency,distance,current_fuel_level):
        self.effciency=effciency
        self.distance=distance
        self.current_fuel_level=current_fuel_level
        self.initial_fuel_level=0
        
    def getGasLevel():
        pass
    def addGas():
        pass     
                
myHybrid = Car(50) # 50 miles per gallon
myHybrid.addGas(20) # Tank 20 gallons
myHybrid.drive(100) # Drive 100 miles
print(myHybrid.getGasLevel()) # Print fuel remaining        