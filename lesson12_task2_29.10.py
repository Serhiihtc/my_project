class Product:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, description={self.description}, dimensions={self.dimensions})"

class Customer:
    def __init__(self, last_name, first_name, middle_name, phone):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.phone = phone

    def __str__(self):
        return f"Customer(last_name={self.last_name}, first_name={self.first_name}, middle_name={self.middle_name}, phone={self.phone})"

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_product(self, product, quantity):
        self.items.append((product, quantity))

    def total_cost(self):
        return sum(product.price * quantity for product, quantity in self.items)

    def __str__(self):
        items_str = "\n".join([f"{product.name} (x{quantity})" for product, quantity in self.items])
        return f"Order for {self.customer.first_name} {self.customer.last_name}:\n{items_str}\nTotal cost: {self.total_cost()}"

product1 = Product("Laptop", 1500, "High performance laptop", "35x25x2 cm")
product2 = Product("Smartphone", 800, "Latest model smartphone", "15x7x0.8 cm")

customer = Customer("Ivanov", "Ivan", "Ivanovich", "+380123456789")

order = Order(customer)
order.add_product(product1, 1)
order.add_product(product2, 2)

print(product1)
print(product2)
print(customer)
print(order)