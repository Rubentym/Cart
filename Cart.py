class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})

    def display_cart(self):
        print("Shopping Cart:")
        for item in self.items:
            print(f"{item['product'].name} - ${item['product'].price} x {item['quantity']}")

# Example usage:
cart = ShoppingCart()
cart.add_to_cart(Product(1, "T-shirt", 20, "Comfortable cotton T-shirt"), 2)
cart.add_to_cart(Product(2, "Jeans", 40, "Classic denim jeans"), 1)
cart.display_cart()
