from xmlrpc.server import SimpleXMLRPCServer
import pickle
import uuid
from datetime import date


class inventory:
    def __init__(self):
        self.names = []
        self.ids = []
        self.manufacturers = {}
        self.products = []
        self.orders = []

    def add_new_product(self, new_product):
        self.products.append(new_product)
        self.names.append(new_product.name)
        self.ids.append(new_product.id_)
        index_of_new_object = len(self.ids) - 1
        if new_product.manufacturer in self.manufacturers.keys():
            self.manufacturers[new_product.manufacturer].append(index_of_new_object)
        else:
            self.manufacturers[new_product.manufacturer] = [index_of_new_object]


class order:
    def __init__(self, destination, products_amount, is_paid=False, is_shipped=False):
        self.id_ = str(uuid.uuid4())
        self.destination = destination
        self.date = date.today()
        self.products_amount = products_amount
        self.is_paid = is_paid
        self.is_shipped = is_shipped

    def update_is_paid(self, is_paid):
        self.is_paid = is_paid

    def update_is_shipped(self, is_shipped):
        self.is_shipped = is_shipped


class product:
    def __init__(self, name, description, manufacturer, sale_cost, whole_sale_cost, amount):
        self.name = name
        self.id_ = str(uuid.uuid4())
        self.amount = amount
        self.description = description
        self.manufacturer = manufacturer
        self.sale_cost = sale_cost
        self.whole_sale_cost = whole_sale_cost

    def change_inventory(self, amount):
        self.amount += amount


products = open("products.txt", "rb")
my_inventory = pickle.load(products)
products.close()



# my_inventory = inventory()

print(my_inventory.names)
print(my_inventory.manufacturers.values())
print(my_inventory.manufacturers.keys())


def add_product(name, description, manufacturer, sale_cost, whole_sale_cost, amount):
    if name not in my_inventory.names:
        new_product = product(name, description, manufacturer, sale_cost, whole_sale_cost, amount)
        my_inventory.add_new_product(new_product)
        return [new_product.id_, new_product.name]
    else:
        return "product already exist"


# TODO refine this one
def list_products():
    summary = []
    for product_ in my_inventory.products:
        summary.append(product_.name)
    return summary


def list_products_by_manufacturer(manufacturer):
    summary = []
    for index in my_inventory.manufacturers[manufacturer]:
        the_product = my_inventory.products[index]
        summary.append(the_product.name + ", " + the_product.description)
    return summary


# TODO refine this one
def lookup_by_name(name):
    if name in my_inventory.names:
        the_product = get_product_by_name(name)
        return the_product.name + ", " + the_product.id_ + ", " + the_product.description


def lookup_by_id(id_):
    if id_ in my_inventory.ids:
        the_product = get_product_by_id(id_)
        return the_product.name + ", " + the_product.description


def get_product_by_id(id_):
    return my_inventory.products[my_inventory.ids.index(id_)]


def get_product_by_name(name):
    return my_inventory.products[my_inventory.names.index(name)]


"""

def increase_inventory(name, amount):
    if name in list_of_products.keys():
        list_of_products.get(name).change_inventory(amount)
        return 1
    else:
        return -1

def decrease_inventory(name, amount):
    if name in list_of_products.keys():
        if amount <= list_of_products.get(name).amount:
            list_of_products.get(name).change_inventory(-amount)
            return 1
        else:
            return -2
    else:
        return -1
        
def list_products(name):
    summary = []
    for name in list_of_products.keys():
        summary.append(get_product(name))
    return summary


# def listProductsWithFilter():
"""

try:

    server = SimpleXMLRPCServer(("localhost", 8000))
    print("Listening on port 8000...")
    server.register_function(add_product, "add_product")
    server.register_function(list_products, "list_products")
    server.register_function(lookup_by_id, "lookup_by_id")
    server.register_function(lookup_by_name, "lookup_by_name")
    server.register_function(list_products_by_manufacturer, "list_products_by_manufacturer")
    # server.register_function(decrease_inventory, "decrease_inventory")
    # server.register_function(increase_inventory, "increase_inventory")
    # server.register_function(list_products, "list_products")
    # server.register_function(listProductsWithFilter, "List of products in the inventory wit a filter")
    server.serve_forever()
except KeyboardInterrupt:
    products = open("products.txt", "wb")
    pickle.dump(my_inventory, products)
    products.close()
