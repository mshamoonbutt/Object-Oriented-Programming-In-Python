"""class Position:
    def __init__(self, initial_point):
        self.initial_point = initial_point
        self.curr_point = initial_point
    
    def turn(self):
        self.curr_point = -self.curr_point
    
    def move(self):
        self.curr_point += 1
    
    def getposition(self):
        return abs(self.curr_point)

position = Position(10)
position.move()
position.move()
position.turn()
position.move()
print(position.getposition())"""

'''class Person:
    def __init__(self, name, y_o_b):
        self.name = name
        self.y_o_b = y_o_b
class Student(Person):
    def __init__(self, name, y_o_b, student_id):
        super().__init__(name, y_o_b)
        self.student_id = student_id
    def __str__(self):
        print("Name: ", self.name, " Year of Birth: ", str(self.y_o_b)," Subject: " ,self.student_id)
print(Student("John", 2000, 1234))'''

# Online Shopping
'''class Product:
    def _init_(self, name, code, price):
        self._name = name
        self._code = code
        self._price = price

class Order:
    def _init_(self):
        self._ordered_products = []

    def add_product(self, product):
        self._ordered_products.append(product)

    def remove_product(self, product_name):
        for product in self._ordered_products:
            if product._name == product_name:
                self._ordered_products.remove(product)
                break

class Customer:
    def _init_(self, username):
        self._username = username

class Invoice:
    _invoice_counter = 0

    def _init_(self, order):
        Invoice._invoice_counter += 1
        self._order = order
        self._invoice_number = Invoice._invoice_counter

class WebShop:
    def _init_(self, products):
        self._products = products

    def login(self, username, password):
        if username == "haroon" and password == "123":
            return Customer(username)
        else:
            return None

    def display_products(self):
        print("Available products:")
        for product in self._products:
            print(f"{product._name} - {product._price}")

    def generate_invoice(self, customer, order):
        invoice = Invoice(order)
        print(f"Invoice generated for customer {customer._username}. Invoice number: {invoice._invoice_number}")

username = input("Enter username: ")
password = input("Enter password: ")

customer = WebShop([]).login(username, password)
if customer:
    print("\nWelcome to Online Shopping!\n")

    products = [
        Product("Chainsaw", "CS001", 59.95),
        Product("Bowie knife", "BK001", 39.95),
        Product("Samurai sword", "SS001", 159.95),
        Product("Axe", "AX001", 29.95),
        Product("Colt 45", "C0001", 299.95),
        Product("Magnum 357", "MG001", 359.95),
        Product("Shotgun", "SG001", 158.00),
        Product("UZZI", "UZ001", 550.95),
        Product("Machete", "MT001", 49.95),
        Product("Sniper rifle", "SR001", 290.95)
    ]

    online_shopping = WebShop(products)
    online_shopping.display_products()

    order = Order()
    while True:
        choice = input("Enter the number of the product to add to your order ('q' to finish): ")
        if choice.lower() == 'q':
            break
        elif choice.isdigit():
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(products):
                selected_product = products[choice_index]
                order.add_product(selected_product)
                print(f"{selected_product._name} added to your order.")
            else:
                print("Invalid product number.")
        else:
            print("Invalid input.")

    print("Your order:")
    for i in range(len(order._ordered_products)):
        print(f"{i+1}. {order._ordered_products[i]._name}")

    while True:
        delete_choice = input("Enter the name of the product to remove from your order ('q' to finish): ")
        if delete_choice.lower() == 'q':
            break
        else:
            order.remove_product(delete_choice)
            print(f"{delete_choice} removed from your order.")

    print("Your updated order:")
    for i in range(len(order._ordered_products)):
        print(f"{i+1}. {order._ordered_products[i]._name}")
    online_shopping.generate_invoice(customer, order)
else:
    print("Invalid username or password.")                    '''
    
class MonsterAcademy:
    def __init__(self):
        self.current_room = "main entrance"

    def start_game(self):
        print("You are at the main entrance of the Monster Academy.")
        choice = input("Do you choose door 1 or door 2? ")

        if choice == '1':
            self.current_room = 'library'
        elif choice == '2':
            self.current_room = 'enchanted garden'
        else:
            print("Invalid input. Please choose door 1 or door 2.")

        if self.current_room == 'library':
            self.library_challenge()
        elif self.current_room == 'enchanted garden':
            self.enchanted_garden()
        elif self.current_room == 'dungeon room':
            self.dungeon_puzzle()
        elif self.current_room == 'treasure room':
            self.treasure_room()

        print("Game over. You have reached the", self.current_room)

    def library_challenge(self):
        riddle_answer = "piano"
        attempts = 0

        while True:
            answer = input("What has keys but can't open locks? ")
            if answer.lower() == riddle_answer:
                self.current_room = "treasure room"
                break
            else:
                attempts += 1
                if attempts >= 10:
                    self.current_room = "dungeon room"
                    break

    def enchanted_garden(self):
        ingredients = ['bat wings', 'eye of newt', 'toe of frog', 'unicorn horn', 'mandrake root']
        correct_ingredient = 'toe of frog'

        print("Available ingredients:")
        for i, ingredient in enumerate(ingredients):
            print(f"{i+1}. {ingredient}")
        choice = int(input("Enter the number of the correct ingredient: "))

        if ingredients[choice-1] == correct_ingredient:
            self.current_room = "treasure room"
        else:
            self.current_room = "dungeon room"

    def dungeon_puzzle(self):
        correct_sequence = ['down', 'up', 'down', 'up']

        print("You've stumbled into a dark dungeon. There are four levers in front of you.")
        print("Each lever needs to be pulled either 'up' or 'down'.")
        print("Enter your sequence (e.g. up up up down):")
        player_sequence = input().split()

        if player_sequence == correct_sequence:
            self.current_room = "treasure room"
        else:
            self.current_room = "main entrance"

    def treasure_room(self):
        correct_sequence = ["Earth", "Water", "Fire", "Air"]
        attempts = 0
        max_attempts = 3

        print("In front of you are four statues, each representing an element.")
        print("Solve the riddle to unlock the treasure.")
        print("Riddle: 'From the ground to the sky, life flows. Begin where it grows and end where it blows.'")

        while attempts < max_attempts:
            player_sequence = input("Enter the elements in the order you think is correct (separated by commas): ").split(", ")

            if player_sequence == correct_sequence:
                print("Congratulations! You have unlocked the treasure!")
                break
            else:
                attempts += 1
                if attempts == max_attempts:
                    self.current_room = "main entrance"
                    break
                else:
                    print("Incorrect sequence. Try again.")


game = MonsterAcademy()
game.start_game()    