import grpc
import inventory_system_pb2
import inventory_system_pb2_grpc
from uuid import uuid4

class Inventory:
    '''
    A class of our inventory, which contains two dictionaries based upon products with their ID
    as a key and with their name as a key, a dictionary for all orders in our inventory, and
    functions which modify or access our inventory.
    '''
    def __init__(self):
        self.products_by_id = {}
        self.products_by_name = {}
        self.orders = {}

    '''
    The following utility functions are useful for adding, getting and modifying products. All of these methods
    recieve the inventory as an argument, we should consider changing this in the future somehow.
    '''
    def get_product(self, name, id_):
        '''
        Gets a specific product from the database using a name or an ID.
        Checks both dictionaries to see if it exists and returns None if it does not.
        '''
        if name in self.products_by_name:
            return self.products_by_name[name]
        elif id_ in self.products_by_id:
            return self.products_by_id[id_]
        else:
            return None

    def add_product(self, product):
        '''
        Adds a product to the database given a product object, adds to both dictionaries
        so we can access by either name or ID. Returns a null identfier if the product
        already exists in the database.
        '''
        if self.is_product(product.name, product.id):
            return "null", "-1"
        self.products_by_id[product.id] = product
        self.products_by_name[product.name] = product
        return product.name, product.id

    def is_product(self, name, id_):
        '''
        Checks to see if a product exists in our inventory.
        Returns false if the product does not exist.
        '''
        if name in self.products_by_name or id_ in self.products_by_id:
            return True
        else:
            return False

    def update_description(self, name, id_, description):
        '''
        Updates a product's description given it's name, ID, and the new description
        Returns false if the product does not exist.
        '''
        if self.is_product(name, id_):
            product = self.get_product(name, id_)
            product.description = description
            return True
        else:
            return False

    def update_manufacturer(self, name, id_, manufacturer):
        '''
        Update's a product's manufacturer given name, ID, and the new manufacturer.
        Returns false if the product does not exist.
        '''
        if self.is_product(name, id_):
            product = self.get_product(name, id_)
            product.manufacturer = manufacturer
            return True
        else:
            return False

    def update_wholesale_cost(self, name, id_, wholesale_cost):
        '''
        Update's a product's wholesale cost given name, ID, and the new wholesale cost.
        Returns false if the product does not exist.
        '''
        if self.is_product(name, id_):
            product = self.get_product(name, id_)
            product.wholesale_cost = wholesale_cost
            return True
        else:
            return False

    def update_sale_cost(self, name, id_, sale_cost):
        '''
        Update's a product's sale cost given name, ID, and the new sale cost.
        Returns false if the product does not exist.
        '''
        if self.is_product(name, id_):
            product = self.get_product(name, id_)
            product.sale_cost = sale_cost
            return True
        else:
            return False

    def increase_product_amount(self, name, id_, amount):
        '''
        Increases the amount of a product given a name, ID, and amount of a product.
        Returns false if the product does not exist.
        '''
        if self.is_product(name, id_):
            product = self.get_product(name, id_)
            product.amount += amount
            return True
        else:
            return False

    def decrease_product_amount(self, name, id_, amount):
        '''
        Decreases the amount of a product given a name, ID, and amount of a product.
        Returns false if the product does not exist or if the product does not have
        stock in inventory to be added.
        '''
        if self.is_product(name, id_):
            product = self.get_product(name, id_)
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
    def add_order(self, order):
        '''
        Checks each product given in an order object, checks to see if they are
        valid and have enough stock to be added to an order, and adds all successful
        products to a given order. Returns -1 as a null id if the order already exists.
        '''
        valid_products = []
        if not self.is_order(order.id):
            for order_product in order.products:
                name = order_product[0]
                id_ = order_product[1]
                amount = order_product[2]
                if self.is_product(name, id_):
                    product = self.get_product(name, id_)
                    if product.amount >= amount:
                        valid_products.append([product.name, product.id, amount])
                        product.amount -= amount
            order.products = valid_products
            self.orders[order.id] = order
            return order.id
        else:
            return "-1"


    def is_order(self, id_):
        '''
        Checks to see if an order exists in inventory,
        returns false if the order already exists.
        '''
        if id_ in self.orders:
            return True
        else:
            return False

    def get_order(self, id_):
        '''
        Gets and order from the database,
        returns false if it does not exist.
        '''
        if self.is_order(id_):
            return self.orders[id_]
        else:
            return None

    def add_product_to_order(self, order_id, new_product_name, new_product_id, new_product_amount):
        '''
        Adds a product to an order, checks to see if a product exists within an order,
        and also checks to see if enough stock is availible for a product to be added. On success,
        adds the product and deducts it's amount from the stock of the product.
        Returns false if there is not enough stock, or if the order does not exist
        '''
        if not self.is_order(order_id):
            return False
        if not self.is_product(new_product_name, new_product_id):
            return False
        order = self.get_order(order_id)
        if len(order.products) != 0:
            for old_product in order.products:
                if new_product_name in old_product or new_product_id in old_product:
                    product = self.get_product(old_product[0], old_product[1])
                    if product.amount >= new_product_amount:
                        product.amount -= new_product_amount
                        old_product[2] += new_product_amount
                        self.orders[order_id] = order
                        return True
                    else:
                        return False
                else:
                    product = self.get_product(new_product_name, new_product_id)
                    if product.amount >= new_product_amount:
                        product.amount -= new_product_amount
                        order.products.append([product.name, product.id, new_product_amount])
                        self.orders[order_id] = order
                        return True
                    else:
                        return False
        else:
            product = self.get_product(new_product_name, new_product_id)
            if product.amount >= new_product_amount:
                product.amount -= new_product_amount
                order.products.append([product.name, product.id, new_product_amount])
                self.orders[order_id] = order
                return True
            else:
                return False

    def remove_product_from_order(self, order_id, new_product_name, new_product_id, new_product_amount):
        '''
        Removes a product from an order given the amount we wish to remove and the product identifier.
        Checks to see if we have enough in the order to remove, if the amount of product we wish to
        remove is equal to the amount in the order, then we simply remove the product.
        Returns false if the product does not exist in the order, if the order does not exist, or if the amount
        we wish to remove is greater than the amount in order.
        '''
        if not self.is_order(order_id):
            return False
        if not self.is_product(new_product_name, new_product_id):
            return False
        order = self.get_order(order_id)
        if (len(order.products) == 0):
            return False
        for old_product in order.products:
            if new_product_name in old_product or new_product_id in old_product:
                product = self.get_product(old_product[0], old_product[1])
                if old_product[2] > new_product_amount:
                    product.amount += new_product_amount
                    old_product[2] -= new_product_amount
                    self.orders[order_id] = order
                    return True
                if old_product[2] == new_product_amount:
                    product.amount += new_product_amount
                    order.products.remove([old_product[0], old_product[1], old_product[2]])
                    self.orders[order_id] = order
                    return True
                else:
                    return False
        return False

    def update_order_destination(self, order_id, destination):
        '''
        Updates the destination of an order given a destination and an order id.
        Fails if the order does not exist.
        '''
        if self.is_order(order_id):
            order = self.get_order(order_id)
            order.destination = destination
            return True
        else:
            return False

    def update_order_date(self, order_id, date):
        '''
        Updates the date of an order given a date and an order id.
        Fails if the order does not exist.
        '''
        if self.is_order(order_id):
            order = self.get_order(order_id)
            order.date = date
            return True
        else:
            return False

    def update_order_paid(self, order_id, is_paid):
        '''
        Updates the paid status of an order given a boolean is_paid and an order id.
        Fails if the order does not exist.
        '''
        if self.is_order(order_id):
            order = self.get_order(order_id)
            order.is_paid = is_paid
            return True
        else:
            return False

    def update_order_shipped(self, order_id, is_shipped):
        '''
        Updates the shipped status of an order given a boolean is_shipped and an order id.
        Fails if the order does not exist.
        '''
        if (self.is_order(order_id)):
            order = self.get_order(order_id)
            order.is_shipped = is_shipped
            return True
        else:
            return False


class Product:
    '''
    Defines a product, each attribute is given in the constructor, except for id which is
    generated as a uuid.
    '''
    def __init__(self, name, amount, description, manufacturer, sale_cost, wholesale_cost):
        self.name = name
        self.id = str(uuid4())
        self.amount = amount
        self.description = description
        self.manufacturer = manufacturer
        self.sale_cost = sale_cost
        self.wholesale_cost = wholesale_cost


class Order:
    '''
    Defines an order, each attribute is given in the constructor, except for id which is generated
    as a uuid.
    '''
    def __init__(self, destination, date, products, is_paid, is_shipped):
        self.id = str(uuid4())
        self.destination = destination
        self.date = date
        self.products = products
        self.is_paid = is_paid
        self.is_shipped = is_shipped


'''
These are utility functions for gRPC methods, simply to convert back and forth between our objects
and the gRPC objects.
'''
def init_product(product):
    '''
    Turns a product object into a Product message for sending on gRPC.
    '''
    return inventory_system_pb2.Product(name=product.name,
                                        id=product.id,
                                        amount=product.amount,
                                        description=product.description,
                                        manufacturer=product.manufacturer,
                                        sale_cost=product.sale_cost,
                                        wholesale_cost=product.wholesale_cost)


def init_order(order):
    '''
    Turns an order object into an Order message for sending on gRPC.
    '''
    product_amounts = []
    for product in order.products:
        product_id = inventory_system_pb2.ProductIdentifier(name=product[0], id=product[1])
        product_amounts.append(inventory_system_pb2.ProductAmount(product_identifier=product_id, amount=product[2]))
    return inventory_system_pb2.Order(id=order.id,
                                      destination=order.destination,
                                      date=order.date,
                                      products=product_amounts,
                                      is_paid=order.is_paid,
                                      is_shipped=order.is_shipped)


def retrieve_product(request):
    '''
    Turns a Product message into a product object for recieving from gRPC.
    '''
    name = request.name
    amount = request.amount
    description = request.description
    manufacturer = request.manufacturer
    sale_cost = request.sale_cost
    wholesale_cost = request.wholesale_cost
    return Product(name, amount, description, manufacturer, sale_cost, wholesale_cost)


def retrieve_order(request):
    '''
    Turns an Order message into an order object for recieving from gRPC.
    '''
    destination = request.destination
    date = request.date
    # products is a repeated struct
    products = []
    for i in request.products:
        products.append([i.product_identifier.name, i.product_identifier.id, i.amount])
    is_paid = request.is_paid
    is_shipped = request.is_shipped
    return Order(destination, date, products, is_paid, is_shipped)
