class Person:
      def __init__(self, name, age):
          self.name = name 
          self.age = age 

      def greet(self): 
          print("Hello, my name is %s!" % self.name)

class TenYearOldPerson(Person):

      def __init__(self, name): 
          Person.__init__(self, name, 10) 

      def greet(self): 
          print("I don't talk to strangers!!")

tyo = TenYearOldPerson("Jack")
tyo.greet()