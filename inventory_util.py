import grpc
import inventory_system_pb2
import inventory_system_pb2_grpc
from uuid import uuid4

null_product = inventory_system_pb2.Product(name = "null", id = "-1", amount = -1, description = "null", manufacturer = "null",
                sale_cost = 0, wholesale_cost = 0)
null_identifier = inventory_system_pb2.ProductIdentifier(name = "null", id = "-1")
null_order = inventory_system_pb2.Order(id = "-1", destination = "N/A", date = "1/1/1970", products = [], is_paid = False, is_shipped = False)


class Product:

    def __init__(self, name, amount, description, manufacturer, sale_cost, wholesale_cost):
        self.name = name
        self.id = str(uuid4())
        self.amount = amount
        self.description = description
        self.manufacturer = manufacturer
        self.sale_cost = sale_cost
        self.wholesale_cost = wholesale_cost
        self.products_by_id = {}
        self.products_by_name = {}


class Order:

    def __init__(self, destination, date, products, is_paid, is_shipped):
        self.id = str(uuid4())
        self.destination = destination
        self.date = date
        self.products = products
        self.is_paid = is_paid
        self.is_shipped = is_shipped



'''
The following utility functions are useful for adding, getting and modifying products.
'''
def get_product(name, id_, inventory):
    if name in inventory.products_by_name:
        return inventory.products_by_name[name]
    elif id_ in inventory.products_by_id:
        return inventory.products_by_id[id_]
    else:
        return None


def is_product(name, id_, inventory):
    if name in inventory.products_by_name or id_ in inventory.products_by_id:
        return True
    else:
        return False

def update_product(product, inventory):
    inventory.products_by_name[product.name] = product
    inventory.products_by_id[product.id] = product


def update_description(name, id_, description, inventory):
    if is_product(name, id_, inventory):
        product = get_product(name, id_, inventory)
        product.description = description
        return True
    else:
        return False


def update_manufacturer(name, id_, manufacturer, inventory):
    if is_product(name, id_, inventory):
        product = get_product(name, id_, inventory)
        product.manufacturer = manufacturer
        return True
    else:
        return False


def update_wholesale_cost(name, id_, wholesale_cost, inventory):
    if is_product(name, id_, inventory):
        product = get_product(name, id_, inventory)
        product.wholesale_cost = wholesale_cost
        return True
    else:
        return False


def update_sale_cost(name, id_, sale_cost, inventory):
    if is_product(name, id_, inventory):
        product = get_product(name, id_, inventory)
        product.sale_cost = sale_cost
        return True
    else:
        return False


def increase_product_amount(name, id_, amount, inventory):
    if is_product(name, id_, inventory):
        product = get_product(name, id_, inventory)
        product.amount += amount
        return True
    else:
        return False


def decrease_product_amount(name, id_, amount, inventory):
    if is_product(name, id_, inventory):
        product = get_product(name, id_, inventory)
        if product.amount - amount >= 0:
            product.amount -= amount
            return True
        else:
            return False
    else:
        return False


'''
These utility methods are related to adding and modifying orders.
'''
# This function will most likely need to be refactored.
def add_order(order, inventory):
    valid_products = []
    if not is_order(order.id, inventory):
        for order_product in order.products:
            name = order_product.product_identifier.name
            id_ = order_product.product_identifier.id
            if is_product(name, id_, inventory):
                product = get_product(name, id_, inventory)
                if product.amount >= order_product.amount:
                    valid_products.append([product.name, product.id, order_product.amount])
                    product.amount -= order_product.amount
        order.products = valid_products
        inventory.orders[order.id] = order
        return order.id
    else:
        return "-1"


def is_order(id_, inventory):
    if id_ in inventory.orders:
        return True
    else:
        return False

def get_order(id_, inventory):
    if is_order(id_, inventory):
        return inventory.orders[id_]
    else:
        return None

def add_product_to_order(order, inventory, new_product_name, new_product_id, new_product_amount):
    for old_product in order.products:
        if new_product_name in old_product or new_product_id in old_product:
            product = get_product(old_product[0], old_product[1], inventory)
            if product.amount >= new_product_amount:
                product.amount -= new_product_amount
                old_product[2] += new_product_amount
                return True
            else:
                return False
        else:
            product = get_product(new_product_name, new_product_id, inventory)
            if product.amount >= new_product_amount:
                product.amount -= new_product_amount
                order.products.append([product.name, product.id, new_product_amount])
                return True
            else:
                return False

def remove_product_from_order(order, inventory, new_product_name, new_product_id, new_product_amount):
    for old_product in order.products:
        if new_product_name in old_product or new_product_id in old_product:
            product = get_product(old_product[0], old_product[1], inventory)
            if old_product[2] > new_product_amount:
                product.amount += new_product_amount
                old_product[2] -= new_product_amount
                return True
            if old_product[2] == new_product_amount:
                product.amount += new_product_amount
                order.products.remove([old_product[0], old_product[1], old_product[2]])
                return True
            else:
                return False
        else:
            return False


def update_order_destination(order_id, inventory, destination):
    if (is_order(order_id, inventory)):
        order = get_order(order_id, inventory)
        order.destination = destination
        return True
    else:
        return False

def update_order_date(order_id, inventory, date):
    if (is_order(order_id, inventory)):
        order = get_order(order_id, inventory)
        order.date = date
        return True
    else:
        return False


def update_order_paid(order_id, inventory, is_paid):
    if (is_order(order_id, inventory)):
        order = get_order(order_id, inventory)
        order.is_paid = is_paid
        return True
    else:
        return False


def update_order_shipped(order_id, inventory, is_shipped):
    if (is_order(order_id, inventory)):
        order = get_order(order_id, inventory)
        order.is_shipped = is_shipped
        return True
    else:
        return False


'''
These are utility functions for gRPC methods, simply to convert back and forth between our objects
and the gRPC objects.
'''
def init_product(product):
    return inventory_system_pb2.Product(name = product.name, id = product.id, amount = product.amount, description = product.description, manufacturer = product.manufacturer,
                sale_cost = product.sale_cost, wholesale_cost = product.wholesale_cost)


def init_order(order):
    product_amounts = []
    for product in order.products:
        product_id = inventory_system_pb2.ProductIdentifier(name = product[0], id = product[1])
        product_amounts.append(inventory_system_pb2.ProductAmount(product_identifier = product_id, amount = product[2]))
    return inventory_system_pb2.Order(id = order.id, destination = order.destination, date = order.date, products=product_amounts,
            is_paid = order.is_paid, is_shipped = order.is_shipped)


def retrieve_product(request):
    name = request.name
    amount = request.amount
    description = request.description
    manufacturer = request.manufacturer
    sale_cost = request.sale_cost
    wholesale_cost = request.wholesale_cost
    return Product(name, amount, description, manufacturer, sale_cost, wholesale_cost)


def retrieve_order(request):
    destination = request.destination
    date = request.date
    # products is a repeated struct
    products = request.products
    is_paid = request.is_paid
    is_shipped = request.is_shipped
    return Order(destination, date, products, is_paid, is_shipped)