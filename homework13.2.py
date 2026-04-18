class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, name, surname, phone_number):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.user = user
        self.products = {}  # {item: quantity}

    def add_item(self, item, quantity):
        self.products[item] = quantity

    def get_total(self):
        total = 0
        for item, quantity in self.products.items():
            total += item.price * quantity
        return total

    def __str__(self):
        result = f"User: {self.user}\nItems:\n"
        for item, quantity in self.products.items():
            result += f"{item.name}: {quantity} pcs.\n"
        return result.strip()


# Testing the classes
lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "medium")

print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)

print(cart)

assert isinstance(cart.user, User) is True, "User instance check"
assert cart.get_total() == 60, "Total should be 60"

cart.add_item(apple, 10)

print(cart)

assert cart.get_total() == 40