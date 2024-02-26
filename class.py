class Rectangle:
    #constructor
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self, length, width):
        area = length * width
        return area    

    def area(self):
        area = self.length * self.width
        return area
    
    
rectangle1= Rectangle(4,3)
print(rectangle1.area())    

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        entered_username = input("Enter your username: ")
        entered_password = input("Enter your password: ")

        if entered_username == self.username and entered_password == self.password:
            print("Login successful!")
        else:
            print("Login failed. Invalid username or password.")

user_login = Login("abc", "123")

user_login.login()

