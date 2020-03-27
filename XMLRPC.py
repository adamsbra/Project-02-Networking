from xmlrpc.server import SimpleXMLRPCServer
import pickle
import uuid
from datetime import date


class inventory:
    def __init__(self):
        self.id_names = {}
        self.manufacturers = set()
        self.products = []
        self.orders = []

    def add_new_product(self, new_product):
        self.products.append(new_product)
        self.id_names[new_product.id_] = new_product.name
        self.manufacturers.add(new_product.manufacturer)


class order:
    def __init__(self, destination, products_amount, is_paid=False, is_shipped=False):
        self.id = str(uuid.uuid4())
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


def add_product(name, description, manufacturer, sale_cost, whole_sale_cost, amount):
    if name not in my_inventory.id_names.keys():
        new_product = product(name, description, manufacturer, sale_cost, whole_sale_cost, amount)
        my_inventory.add_new_product(new_product)
        return [new_product.id_, new_product.name]
    else:
        return "product already exist"


def list_products():
    summary = []
    for product in my_inventory.products:
        summary.append(product.name)
    return summary


print(my_inventory.id_names)

"""

def increase_inventory(name, amount):
    if name in list_of_products.keys():
        list_of_products.get(name).change_inventory(amount)
        return 1
    else:
        return -1






def gp_name(name):
    return list_of_products.get(name).name


def gp_amount(name):
    return list_of_products.get(name).amount


def gp_manufacturer(name):
    return list_of_products.get(name).manufacturer


def gp_desc(name):
    return list_of_products.get(name).description


def gp_sale_price(name):
    return list_of_products.get(name).sale_price


def get_product(name):
    return "{0}: {1} units".format(gp_name(name), gp_amount(name))

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
    # server.register_function(lookup_by_id, "lookup_by_id")

    # server.register_function(decrease_inventory, "decrease_inventory")
    # server.register_function(increase_inventory, "increase_inventory")
    # server.register_function(list_products, "list_products")
    # server.register_function(listProductsWithFilter, "List of products in the inventory wit a filter")
    server.serve_forever()
except KeyboardInterrupt:
    products = open("products.txt", "wb")
    pickle.dump(my_inventory, products)
    products.close()
