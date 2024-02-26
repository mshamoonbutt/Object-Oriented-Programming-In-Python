class Address:
    def __init__(self, house_number, street, city, state, postal_code, apartment_number=None):
        self.house_number = house_number
        self.street = street
        self.apartment_number = apartment_number
        self.city = city
        self.state = state
        self.postal_code = postal_code

    def print_address(self):
        print(f"{self.house_number} {self.street}")
        if self.apartment_number is not None:
            print(f"Apartment {self.apartment_number}")
        print(f"{self.city}, {self.state} {self.postal_code}")

    def comes_before(self, other):
        return self.postal_code < other.postal_code

# Example usage:
address1 = Address(123, "Main St", "Cityville", "CA", "12345")
address2 = Address(456, "Maple St", "Townsville", "NY", "67890", apartment_number=789)

address1.print_address()
print("\n")
address2.print_address()

if address1.comes_before(address2):
    print("\nAddress 1 comes before Address 2.")
else:
    print("\nAddress 2 comes before Address 1.")
