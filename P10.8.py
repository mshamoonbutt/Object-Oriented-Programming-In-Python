class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob
        
    def __repr__(self):
        return f"Name: {self.name}, Year of Birth: {self.yob}"
        
class Student(Person):
    def __init__(self, name, yob, major):
        super().__init__(name, yob)
        self.major = major
        
    def __repr__(self):
        return super().__repr__() + f", Major: {self.major}"
        
class Instructor(Person):
    def __init__(self, name, yob, salary):
        super().__init__(name, yob)
        self.salary = salary
        
    def __repr__(self):
        return super().__repr__() + f", Salary: {self.salary}"

# Test program
person = Person("John Doe", 1990)
print(person)

student = Student("Jane Smith", 1995, "Computer Science")
print(student)

instructor = Instructor("Bob Johnson", 1985, 50000)
print(instructor)