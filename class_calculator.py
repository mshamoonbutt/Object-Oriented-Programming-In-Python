class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b    
    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return ("Cannot divide by zero.")
        
calculator = Calculator()
result = calculator.add(7, 5)
print("7 + 5 =", result)

result = calculator.subtract(34, 21)
print("34 - 21 =", result)

result = calculator.multiply(54, 2)
print("54 * 2 =", result)

result = calculator.divide(144, 2)
print("144 / 2 =", result)

result = calculator.divide(1, 2)
print("1 / 2 =", result)        