from datetime import date

import pickle
import uuid
import inventory_util as ui

# assumptions (to maybe be fixed):
# once a product or manufacturer is created they are never eliminated even if it reaches 0 units, they will just empty
inventory_xml = None


def get_order(id_):
    return inventory_xml.get_order(id_)


def get_product(name, id_):
    return inventory_xml.get_product(name, id_)


def add_order(products, destination, is_paid=False, is_shipped=False):
    order = ui.Order(destination, date, products, is_paid, is_shipped)
    # returns order id otherwise returns -1
    order_id = inventory_xml.add_order(order)
    return order_id


def add_product(name, description, manufacturer, sale_cost, whole_sale_cost, amount):
    product = ui.Product(name, amount, description, manufacturer, sale_cost, whole_sale_cost)
    name_ID = inventory_xml.add_product(product)
    return name_ID


def is_a_product(name, id_):
    return inventory_xml.is_product(name, id_)


def decrease_product_amount(name, id_, amount):
    success = inventory_xml.decrease_product_amount(name, id_, amount)
    return success


def increase_product_amount(name, id_, amount):
    success = inventory_xml.increase_product_amount(name, id_, amount)
    return success


def update_description(name, id_, description):
    success = inventory_xml.update_description(name, id_, description)
    return success


def update_sale_cost(name, id_, sale_cost):
    success = inventory_xml.update_sale_cost(name, id_, sale_cost)
    return success


def update_manufacturer(name, id_, manufacturer):
    success = inventory_xml.update_manufacturer(name, id_, manufacturer)
    return success


def update_wholesale_cost(name, id_, wholesale_cost):
    success = inventory_xml.update_wholesale_cost(name, id_, wholesale_cost)
    return success


def add_product_to_order(order_id, new_product_name, new_product_id, new_product_amount):
    success = inventory_xml.add_product_to_order(order_id, new_product_name, new_product_id, new_product_amount)
    return success


def remove_product_from_order(order_id, new_product_name, new_product_id, new_product_amount):
    success = remove_product_from_order(order_id, new_product_name, new_product_id, new_product_amount)
    return success


def update_order_destination(order_id, destination):
    success = inventory_xml.update_order_destination(order_id, destination)
    return success


def update_order_date(order_id, date_):
    success = inventory_xml.update_order_date(order_id, date_)
    return success


def update_order_paid(order_id, is_paid):
    success = inventory_xml.update_order_paid(order_id, is_paid)
    return success


def update_order_shipped(order_id, is_shipped):
    success = inventory_xml.update_order_shipped(order_id, is_shipped)
    return success


# Todo
def get_order_summary(id_):
    order_ = get_order(id_)
    summary = "ID: " + str(order_.id) + " "
    for product in order_.products:
        summary += product.name+ ": " + product.amount + " units. "
    return summary


# TODO refine
def get_product_summary(name, id):
    the_product = get_product(name, id)
    return the_product.name + ", has " + str(
        the_product.amount) + " units, manufacturer:" + the_product.manufacturer + ", ID:" + the_product.id + \
           ", description: " + the_product.description + \
           ", whole Sale and sale cost:" + str(the_product.whole_sale_cost) + " " + str(the_product.sale_cost)


def list_products():
    products = []
    for product_ in inventory_xml.products_by_id.values():
        products.append(product_.name)
    return products


def list_orders():
    orders = []
    for product_ in inventory_xml.orders.values():
        orders.append(product_.id)
    return orders



def list_products_by_manufacturer(manufacturer):
    products_by_manufacturer = []
    for product in inventory_xml.products_by_id.values():
        if product.manufacturer == manufacturer:
            products_by_manufacturer.append(product)
    return products_by_manufacturer



def list_unshipped():
    unshipped_orders = []
    for order in inventory_xml.orders.values():
        if not order.is_shipped:
            unshipped_orders.append(order)
    return unshipped_orders


def list_unpaid():
    unpaid_orders = []
    for order in inventory_xml.orders.values():
        if not order.is_paid:
            unpaid_orders.append(order)
    return unpaid_orders


def start_xml(server, inventory):
    global inventory_xml
    inventory_xml = inventory
    server.register_function(add_order, "add_order")
    server.register_function(add_product, "add_product")
    server.register_function(update_description, "update_description")
    server.register_function(update_manufacturer, "update_manufacturer")
    server.register_function(update_sale_cost, "update_sale_cost")
    server.register_function(update_wholesale_cost, "update_wholesale_cost")
    server.register_function(increase_product_amount, "increase_product_amount")
    server.register_function(list_products, "list_products")
    server.register_function(list_products_by_manufacturer, "list_products_by_manufacturer")
    server.register_function(get_order_summary, "get_order")
    server.register_function(get_product_summary, "get_product")
    server.register_function(decrease_product_amount, "decrease_product_amount")
    server.register_function(list_unshipped, "list_unshipped")
    server.register_function(list_unpaid, "list_unpaid")
