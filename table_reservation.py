class Table:
    def __init__(self, table_no, capacity):
        self.table_no = table_no
        self.capacity = capacity

class Reservation:
    def __init__(self, customer, table, time_slot, no_of_people):
        self.customer = customer
        self.table = table
        self.time_slot = time_slot
        self.no_of_people = no_of_people

    def add_reservation(self):
        print(f"Reservation for {self.customer.name} has been added.")

    def cancel_reservation(self):
        print(f"Reservation for {self.customer.name} has been cancelled.")

class Customer:
    def __init__(self, name):
        self.name = name

class Staff:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Waiter(Staff):
    def serve_customer(self, table):
        print(f"{self.name} is serving customers at table {table.table_no}.")

    def take_order(self, customer, order):
        print(f"{self.name} is taking order from {customer.name}. Order: {order}")

class Chef(Staff):
    def prep_food(self):
        print(f"{self.name} is preparing food.")

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.tables = []
        self.reservations = []

    def add_table(self, table):
        self.tables.append(table)
        print(f"Table {table.table_no} has been added to {self.name}.")

    def add_reservation(self, reservation):
        self.reservations.append(reservation)
        print(f"Reservation for {reservation.customer.name} has been added.")

    def cancel_reservation(self, reservation):
        self.reservations.remove(reservation)
        print(f"Reservation for {reservation.customer.name} has been cancelled.")

restaurant = Restaurant("The Food Place")
table1 = Table(1, 4)
table2 = Table(2, 2)

restaurant.add_table(table1)
restaurant.add_table(table2)

customer1 = Customer("Alice")
customer2 = Customer("Bob")

reservation1 = Reservation(customer1, table1, "19:00", 2)
reservation2 = Reservation(customer2, table2, "20:00", 2)

restaurant.add_reservation(reservation1)
restaurant.add_reservation(reservation2)

waiter = Waiter("John", "W001")
chef = Chef("Emily", "C001")

waiter.serve_customer(table1)
waiter.take_order(customer1, ["Pizza", "Salad"])

chef.prep_food()
restaurant.cancel_reservation(reservation2)
