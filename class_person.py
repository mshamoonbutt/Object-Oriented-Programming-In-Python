class Person:

     def __init__(self, name, age): # class constructor
         self.name = name # class variable
         self.age = age # class variable

     def greet(self): # class function to print a greeting
         print("Hello, my name is %s!" % self.name)
        

a = Person("Peter", 20) # instantiation
b = Person("Anna", 19) # instantiation

a.greet() # call a's greet method
b.greet() # call b's greet method

print(a.name)
print(a.age)  # We can also access the attributes of an object

print(b.name)
print(b.age)  # We can also access the attributes of an object