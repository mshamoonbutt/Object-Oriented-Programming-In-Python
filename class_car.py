class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        
    def display(self):
        print("Make:", self.make)
        print("Model:", self.model)
        print("Year:",self.year)
        
a=Car("Honda","V8","2021")
a.display()            
a=Car("Audi","GT","2023")
a.display()