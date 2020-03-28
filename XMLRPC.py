from datetime import date
from xmlrpc.server import SimpleXMLRPCServer
import pickle
import uuid


# assumptions (to maybe be fixed):
# once a product or manufacturer is created they are never eliminated even if it reaches 0 units, they will just empty

class inventory:
    def __init__(self):
        self.products = []
        self.names = []
        self.ids = []
        self.manufacturers = {}

        self.orders = []
        self.orders_ids = []
        self.unshipped = []
        self.unpaid = []

    def add_new_product(self, new_product):
        self.products.append(new_product)
        self.names.append(new_product.name)
        self.ids.append(new_product.id_)
        self.update_manufacturers(new_product)

    def add_new_order(self, new_order):
        self.orders.append(new_order)
        self.orders_ids.append(new_order.id_)
        if not new_order.is_shipped:
            self.unshipped.append(self.orders.index(new_order))
        if not new_order.is_paid:
            self.unpaid.append((self.orders.index(new_order)))

    def update_manufacturers(self, the_product):
        index_of_new_object = self.products.index(the_product)
        if the_product.manufacturer in self.manufacturers.keys():
            self.manufacturers[the_product.manufacturer].append(index_of_new_object)
        else:
            self.manufacturers[the_product.manufacturer] = [index_of_new_object]


class order:
    def __init__(self, products_name_or_id, amounts, destination, is_paid, is_shipped):
        self.id_ = str(uuid.uuid4())
        self.destination = destination
        self.date = str(date.today())
        self.products_name_or_id = products_name_or_id
        self.amounts = amounts
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


# TODO might want to change products_name_or_id, amounts lists for a dict or a list of tuples

def add_order(products_name_or_id, amounts, destination, is_paid=False, is_shipped=False):
    orders_products = []
    for product_identifier in products_name_or_id:
        a_product = get_product(product_identifier)
        order_amount = amounts[products_name_or_id.index(product_identifier)]
        if (not is_a_product(a_product)) or (a_product.amount < order_amount):
            return False
        orders_products.append(a_product)

    for product_ in orders_products:
        product_.amount -= amounts[orders_products.index(product_)]

    new_order = order(products_name_or_id, amounts, destination, is_paid, is_shipped)
    my_inventory.add_new_order(new_order)
    return [new_order.id_, new_order.date]


def add_product(name, description, manufacturer, sale_cost, whole_sale_cost, amount):
    if name not in my_inventory.names:
        new_product = product(name, description, manufacturer, sale_cost, whole_sale_cost, amount)
        my_inventory.add_new_product(new_product)
        return [new_product.id_, new_product.name]
    else:
        return "product already exist"


def change_amount(name_or_id, amount):
    the_product = get_product(name_or_id)
    if is_a_product(the_product):
        if (the_product.amount + amount) >= 0:
            the_product.amount += amount
            return True
        else:
            return False  # trying to subtract more than current stock
    else:
        return False  # name or id not found


def change_description(name_or_id, description):
    the_product = get_product_summary(name_or_id)
    if is_a_product(the_product):
        the_product.description = description
    else:
        return False  # name or id not found


def change_manufacturer(name_or_id, new_manufacturer):
    the_product = get_product(name_or_id)
    if is_a_product(the_product):

        # remove the product from the old manufacturer list
        my_inventory.manufacturers[the_product.manufacturer].remove(my_inventory.products.index(the_product))
        the_product.manufacturer = new_manufacturer
        my_inventory.update_manufacturers(the_product)
        return True
    else:
        return False  # name or id not found


def change_sale_cost(name_or_id, new_sale_cost):
    the_product = get_product(name_or_id)
    if is_a_product(the_product):
        the_product.sale_cost = new_sale_cost
        return True
    else:
        return False


def change_wholesale_cost(name_or_id, new_whole_sale_cost):
    the_product = get_product(name_or_id)
    if is_a_product(the_product):
        the_product.whole_sale_cost = new_whole_sale_cost
        return True
    else:
        return False


def lookup_order(id_):
    if id_ in my_inventory.orders_ids:
        the_order = get_order(id_)
        return get_order_summary(the_order)


def get_order(id_):
    return my_inventory.orders[my_inventory.orders_ids.index(id_)]


def get_order_summary(order_):
    summary = "ID: " + str(order_.id_) + " "
    for i in range(len(order_.amounts)):
        summary += order_.products_name_or_id[i] + ": " + str(order_.amounts[i]) + " units. "
    return summary


def get_product(name_or_id):
    if name_or_id in my_inventory.names:
        return get_product_by_name(name_or_id)
    elif name_or_id in my_inventory.ids:
        return get_product_by_id(name_or_id)
    else:
        return False


def get_product_by_id(id_):
    return my_inventory.products[my_inventory.ids.index(id_)]


def get_product_by_name(name):
    return my_inventory.products[my_inventory.names.index(name)]


# TODO refine
def get_product_summary(the_product):
    return the_product.name + ", has " + str(
        the_product.amount) + " units, manufacturer:" + the_product.manufacturer + ", ID:" + the_product.id_ + \
           ", description: " + the_product.description + \
           ", whole Sale and sale cost:" + str(the_product.whole_sale_cost) + " " + str(the_product.sale_cost)


def is_a_product(product_or_boolean):
    return isinstance(product_or_boolean, product)


def increase_amount(name_or_id, amount):
    print(amount)
    transaction_success = change_amount(name_or_id, amount)
    return transaction_success


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
def lookup_product_by_name(name):
    if name in my_inventory.names:
        the_product = get_product_by_name(name)
        return get_product_summary(the_product)


def lookup_product_by_id(id_):
    if id_ in my_inventory.ids:
        the_product = get_product_by_id(id_)
        return get_product_summary(the_product)


def lower_amount(name_or_id, amount):
    transaction_success = change_amount(name_or_id, -amount)
    return transaction_success


def list_unshipped():
    unshipped = []
    for i in my_inventory.unshipped:
        unshipped.append(get_order_summary(my_inventory.orders[i]))
    return unshipped


def list_unpaid():
    unpaid = []
    for i in my_inventory.unpaid:
        unpaid.append(get_order_summary(my_inventory.orders[i]))
    return unpaid


try:

    server = SimpleXMLRPCServer(("localhost", 8000))
    print("Listening on port 8000...")
    server.register_function(add_order, "add_order")
    server.register_function(add_product, "add_product")
    server.register_function(change_description, "change_description")
    server.register_function(change_manufacturer, "change_manufacturer")
    server.register_function(change_sale_cost, "change_sale_cost")
    server.register_function(change_wholesale_cost, "change_wholesale_cost")
    server.register_function(increase_amount, "increase_amount")
    server.register_function(list_products, "list_products")
    server.register_function(list_products_by_manufacturer, "list_products_by_manufacturer")
    server.register_function(lookup_order, "lookup_order")
    server.register_function(lookup_product_by_id, "lookup_product_by_id")
    server.register_function(lookup_product_by_name, "lookup_product_by_name")
    server.register_function(lower_amount, "lower_amount")
    server.register_function(list_unshipped, "list_unshipped")
    server.register_function(list_unpaid, "list_unpaid")

    server.serve_forever()
except KeyboardInterrupt:
    products = open("products.txt", "wb")
    pickle.dump(my_inventory, products)
    products.close()
