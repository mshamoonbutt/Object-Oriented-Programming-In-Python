class Product:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product): 
        self.products.append(product)

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                break

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

class Invoice:
    invoice_counter = 1

    def __init__(self, order):
        self.order = order
        self.invoice_number = Invoice.invoice_counter
        Invoice.invoice_counter += 1

    def generate_invoice(self):
        print(f"Invoice Number: {self.invoice_number}")
        print("Ordered Products:")
        for product in self.order.products:
            print(f"{product.name}: ${product.price}")
        print(f"Total: ${self.order.calculate_total()}")

class Customer:
    def __init__(self, name):
        self.name = name

class Shop:
    def __init__(self, products):
        self.products = products

    def display_products(self):
        print("Available Products:")
        for product in self.products:
            print(f"{product.name}: ${product.price}")

    def login(self, username, password):
        # Simulated login process
        return Customer(username)

# Sample products
products_list = [
    Product("001", "Biscuit", 50),
    Product("002", "Cold Drink", 100),
    Product("003", "Candy", 10),
    Product("003", "Lays", 60),
    Product("003", "Cake", 300),
    Product("003", "Pizza", 500)
]

# Main program
def main():
    # Initialize shop with products
    shop = Shop(products_list)

    # Login
    username = input("Enter username: ")
    password = input("Enter password: ")
    customer = shop.login(username, password)

    if customer:
        print(f"Welcome, {customer.name}!\n")

        # Display available products
        shop.display_products()

        # Create order
        order = Order()

        # Add products to the order
        while True:
            # Display available products
            shop.display_products()

            # Create order
            order = Order()

            # Add products to the order
            while True:
                product_name = input("\nEnter product name to add (or 'quit' to finish): ")
                if product_name.lower() == "quit":
                    break
                else:
                    for product in products_list:
                        if product.name == product_name:
                            order.add_product(product)
                            break

            # Display current order
            print("\nCurrent Order:")
            for product in order.products:
                print(product.name)

            # Remove products from the order
            while True:
                product_name = input("\nEnter product name to remove (or 'quit' to finish): ")
                if product_name.lower() == "quit":
                    break
                else:
                    order.remove_product(product_name)

            # Generate invoice
            invoice = Invoice(order)
            invoice.generate_invoice()

    else:
        print("Invalid username or password.")

if __name__ == "__main__":
    main()
