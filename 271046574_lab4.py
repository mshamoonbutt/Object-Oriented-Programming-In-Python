'''1. Create a class `Calculator` with methods of Adding, Subtracting, Multiply and Divide.
a. Bonus: Add a method to calculate the Square Root of a number'''

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def subtract(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b    
    def divide(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return ("Cannot divide by zero.")
    def square_root(self):
        return self.a ** 0.5, self.b ** 0.5    
        
calculator = Calculator(16, 4)
print("Sum = ", calculator.add())
print("Difference = ",calculator.subtract())
print("Product = ", calculator.multiply())
print("Divide = ", calculator.divide())
print("Square Roots = ", calculator.square_root())
  


'''2. Create a class `Triangle` with attributes side1, side2, and side3. Include a method
`isValid` to check if the given sides can form a valid triangle. Extend this by adding a
method `typeOfTriangle` that determines whether the triangle is equilateral, isosceles, or
scalene.'''

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1= side1
        self.side2= side2
        self.side3= side3
    def isValid(self):
        if self.side1 + self.side2 > self.side3 or self.side2 + self.side3 > self.side1 or self.side1 + self.side3 > self.side2:
            return True
        else:
            return False  
    def typeOfTriangle(self):
        if self.side1 == self.side2 == self.side3:
            return "Equilateral"
        elif self.side1 == self.side2 or self.side2 == self.side3 or self.side1 == self.side3:
            return "Isosceles"
        else:
            return "Scalene"  
triangle = Triangle(3, 3, 3)
if triangle.isValid():
    print("Valid Triangle")
else:
    print("Invalid Triangle")    
print("Type Of Triangle is", triangle.typeOfTriangle())  

'''3. Write a Python program to create a `Person` class. Include attributes like name, country
and DOB. Implement a method to determine the person’s age'''

class Person:
    def __init__(self, name, country, d_o_b):
        self.name = name
        self.country = country
        self.d_o_b = d_o_b
    def age(self):
        current_year = 2024
        current_month = 3
        current_date = 20
        birth_year = int(self.d_o_b[-4:])
        birth_month = int(self.d_o_b[3:5])
        birth_date = int(self.d_o_b[:2]) 
        age = current_year - birth_year        
        if birth_month < current_month or (birth_month == current_month and birth_date < current_date):
            age -= 1      
        return age   
person = Person("Ali", "Pakistan", "20-03-2000")
print("Age =", person.age())
person = Person("Ali", "Pakistan", "19-03-2000")
print("Age =", person.age())

'''4. Write a Python program to create a class representing a `Bank`. Include methods for
managing customer accounts and transactions.
a. Create a `createAccount` method to create an account with an account number
and an initial balance of 0, You must check whether an account already exists for
that customer or not.
b. Create a `makeDeposit` method that will increment the initial/existing balance for
that Customers account
c. Create a `makeWithdrawal` method that will allow the user to withdraw a certain
amount while also making sure that it does not allow the users bank balance to
drop below 0 and also set a withdrawal limit per transaction.
d. Create a `checkBalance` method that will return the bank balance for said
account.
e. Bonus: Allow for the setting of different limits for different account types (e.g.,
regular account, premium account).
'''

class Bank:
    def __init__(self):
        self.accounts = {}
    def createAccount(self, account_number, account_type = 'regular'):
        if account_number in self.accounts:
            return "Account already exists"
        else:
            if account_type == 'regular':
                self.accounts[account_number] = {'balance': 0, 'withdrawal_limit': 1000}
            elif account_type == 'premium':
                self.accounts[account_number] = {'balance': 0, 'withdrawal_limit': 5000}
            else:
                return "Invalid account type"
            return "Account created successfully"
    def makeDeposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            return "Deposit successful"
        else:
            return "Account does not exist"
    def makeWithdrawal(self, account_number, amount):
        if account_number in self.accounts:
            if amount <= self.accounts[account_number]['balance']:
                if amount <= self.accounts[account_number]['withdrawal_limit']:
                    self.accounts[account_number]['balance'] -= amount
                    return "Withdrawal successful"
                else:
                    return "Exceeded withdrawal limit"
            else:
                return "Insufficient balance"
        else:
            return "Account does not exist"
    def checkBalance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]['balance']
        else:
            return "Account does not exist"
        
bank = Bank()
print(bank.createAccount(123, 'regular'))
print(bank.makeDeposit(123, 1000))
print(bank.makeWithdrawal(123, 500))
print(bank.checkBalance(123))
print(bank.makeWithdrawal(123, 2000))  
print(bank.createAccount(123))  

print(bank.createAccount(456, 'premium'))
print(bank.makeDeposit(456, 1000))
print(bank.makeWithdrawal(456, 2000))
print(bank.checkBalance(456))      
             
'''5. Create a class called `Car` to model a vehicle's fuel consumption and mileage.
The class should include attributes such as fuel capacity, mileage, and engine
efficiency.
a. Implement a method to initialize a Car object with parameters for fuel
level and engine efficiency. Hint: Use the following formula to calculate
the engine efficiency:
𝑬𝒏𝒈𝒊𝒏𝒆 𝑬𝒇𝒇𝒊𝒄𝒊𝒆𝒏𝒄𝒚 (%) =
𝑻𝒐𝒕𝒂𝒍 𝑫𝒊𝒔𝒕𝒂𝒏𝒄𝒆 𝑻𝒓𝒂𝒗𝒆𝒍𝒆𝒅
𝑭𝒖𝒆𝒍 𝑪𝒐𝒏𝒔𝒖𝒎𝒆𝒅 ∗ 𝟏𝟎𝟎
b. Include a method to calculate how far the car can travel based on its
current fuel level and engine efficiency. Assume that the car consumes
fuel at a constant rate per kilometer.
c. Extend the class by adding a method to update the fuel level when
refueling the car.
d. Implement a method to calculate the car's mileage (kilometers per liter)
based on the distance traveled and the fuel consumed.
e. Bonus: Enhance the class by adding features such as tracking total
distance traveled, average mileage over time, and providing warnings
when fuel levels are low.'''             

class Car:
    def __init__(self, fuel_capacity, total_distance_traveled, fuel_consumed):
        self.fuel_capacity = fuel_capacity
        self.total_distance_traveled = total_distance_traveled
        self.fuel_consumed = fuel_consumed
        self.engine_efficiency = (total_distance_traveled / fuel_consumed) * 100 if fuel_consumed != 0 else 0
        self.current_fuel_level = 0
    
    def initialize(self, fuel_level):
        if 0 <= fuel_level <= self.fuel_capacity:
            self.current_fuel_level = fuel_level
            return "Car initialized successfully"
        else:
            return "Invalid fuel level"
    def engineEfficiency(self):
        if self.total_distance_traveled == 0:
            return "Engine efficiency cannot be calculated as no distance has been traveled yet"
        else:
            return (self.total_distance_traveled / self.fuel_consumed) * 100
    
    def travel_distance(self, distance):
        if self.current_fuel_level == 0:
            return "Cannot travel, fuel level is 0"
        else:
            max_distance = self.current_fuel_level * (self.total_distance_traveled / self.fuel_consumed)
            if distance <= max_distance:
                self.total_distance_traveled += distance
                self.current_fuel_level -= distance / (self.total_distance_traveled / self.fuel_consumed)
                return "Traveled {:.2f} kilometers".format(distance)
            else:
                return "Cannot travel, insufficient fuel"
    
    def refuel(self, fuel_added):
        if 0 <= fuel_added <= (self.fuel_capacity - self.current_fuel_level):
            self.current_fuel_level += fuel_added
            return "Refueling successful"
        else:
            return "Invalid fuel amount"
    
    def calculate_mileage(self):
        if self.total_distance_traveled == 0:
            return "Mileage cannot be calculated, no distance traveled yet"
        else:
            return self.total_distance_traveled / self.fuel_consumed
    
    def low_fuel_warning(self):
        if self.current_fuel_level < 0.1 * self.fuel_capacity:
            return "Low fuel warning: Current fuel level is {:.2f} liters".format(self.current_fuel_level)
        else:
            return "Fuel level is sufficient"

# Test the Car class
car = Car(fuel_capacity=50, total_distance_traveled=100, fuel_consumed=10)  # 10 kilometers per liter efficiency
car.initialize(30)
print(car.travel_distance(200))
print(car.refuel(20))
print(car.travel_distance(100))
print(car.calculate_mileage())
print(car.low_fuel_warning())
print(car.engineEfficiency())

#Another ssolution for same question
class Car:
    def __init__(self, fuel_capacity, current_fuelLevel, total_distance_traveled):
        self.fuel_capacity = fuel_capacity
        self.current_fuelLevel = current_fuelLevel
        self.total_distance_traveled = total_distance_traveled
        self.fuel_consumed = total_distance_traveled/100
    def engineEfficiency(self):
        self.engine_efficiency = (self.total_distance_traveled / self.fuel_consumed) * 100
        return self.engine_efficiency
    
    def travel_distance(self):
        distance = self.current_fuelLevel * (self.total_distance_traveled / self.current_fuelLevel)
        return "Car can travel {:.2f} miles".format(distance)
    
    def refuel(self, fuel_added):
        if 0 <= fuel_added <= (self.fuel_capacity - self.current_fuelLevel):
            self.current_fuelLevel += fuel_added
            return "Refueling successful"
        else:
            return "Invalid fuel amount"      

    def calculate_mileage(self):
        if self.total_distance_traveled > 0:
            return self.total_distance_traveled / self.fuel_consumed
        else:
            return "Mileage cannot be calculated as no distance has been traveled yet"

# Test the Car class
car = Car(50, 20, 10)
print(car.engineEfficiency())
print(car.travel_distance())
print(car.refuel(20))
print(car.calculate_mileage())