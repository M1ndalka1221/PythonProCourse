import json
from typing import List, Dict
import os

class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def change_price(self, new_price):
        if new_price < 0:
            raise ValueError("Invalid price")
        self.price = new_price

    def change_quantity(self, new_quantity):
        if new_quantity < 0:
            raise ValueError("Invalid quantity")
        self.quantity = new_quantity

    def __repr__(self):
        return f"Product {self.name} {self.category} {self.price} {self.quantity}"

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.list_of_orders: List[Order] = []

    def add_order(self, order):
        self.list_of_orders.append(order)

    def __repr__(self):
        return f"Customer {self.name}, count of orders={len(self.list_of_orders)}"


class Order:
    def __init__(self):
        self.products: List[Product] = []
        self.sum_of_order = 0

    def add_product(self, product: Product):
        if product.quantity <= 0:
            print("Product is out of stock")
            return

        self.products.append(product)
        product.change_quantity(product.quantity - 1)

        self.calculate_total_price()

    def calculate_total_price(self):
        self.sum_of_order = sum(product.price for product in self.products)
        return self.sum_of_order

    def __repr__(self) -> str:
        product_names = [p.name for p in self.products]
        return f"{product_names}, {self.sum_of_order})"

class Store:
    def __init__(self):
        self.products: Dict[str, Product] = {}
        self.customers: Dict[str, Customer] = {}

    def load_from_file(self, filepath):
        if not os.path.exists(filepath):
            raise ValueError("File does not exist")
        with open(filepath, 'r', encoding="UTF-8") as file:
            data = json.load(file)

        for product_data in data.get("products", []):
            product = Product(
                name = product_data["name"],
                category = product_data["category"],
                price = product_data["price"],
                quantity= product_data["quantity"]
            )
            self.products[product.name] = product

        for customer_data in data.get("customers", []):
            customer = Customer(
                name = customer_data["name"],
                email = customer_data["email"]
            )
            self.customers[customer.name] = customer

        print(f"Store successfully loaded: {len(self.products)} products, {len(self.customers)} customers.")

    def get_product(self, name):
            return self.products.get(name)

    def get_customer(self, name):
            return self.customers.get(name)


if __name__ == "__main__":
    my_store = Store()
    try:
        my_store.load_from_file('store_data.txt')
    except Exception as e:
        print(f"Loading error: {e}")
        exit()

    customer_alex = my_store.get_customer("Alexander")
    bear = my_store.get_product("Teddy Bear")
    lego = my_store.get_product("LEGO City")

    print("\nBefore shopping:")
    print(bear)
    print(lego)

    new_order = Order()

    new_order.add_product(bear)
    new_order.add_product(bear)
    new_order.add_product(lego)

    customer_alex.add_order(new_order)

    print("\nAfter shopping:")
    print(f"Alexander's order: {new_order}")
    print(bear)
    print(lego)

    print("\nPrice change by manager:")
    bear.change_price(400.0)
    print(bear)

