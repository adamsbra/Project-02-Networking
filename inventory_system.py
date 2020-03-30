import grpc
import inventory_system_pb2
import inventory_system_pb2_grpc
import pickle
import os
from uuid import uuid4
from concurrent import futures
from inventory_util import *



class InventorySystem(inventory_system_pb2_grpc.InventorySystemServicer):


    null_product = inventory_system_pb2.Product(name = "null", id = "-1", amount = -1, description = "null", manufacturer = "null",
                sale_cost = 0, wholesale_cost = 0)
    null_identifier = inventory_system_pb2.ProductIdentifier(name = "null", id = "-1")
    null_order = inventory_system_pb2.Order(id = "-1", destination = "N/A", date = "1/1/1970", products = [], is_paid = False, is_shipped = False)


    def GetProduct(self, request, context):
        name = request.name
        id_ = request.id
        if is_product(name, id_, inventory):
            return init_product(get_product(name, id_, inventory))
        else:
            return self.null_product


    def AddProduct(self, request, context):
        new_product = retrieve_product(request)
        if is_product(new_product.name, new_product.id, inventory):
            return self.null_identifier
        inventory.products_by_id[new_product.id] = new_product
        inventory.products_by_name[new_product.name] = new_product
        return inventory_system_pb2.ProductIdentifier(name = new_product.name, id = new_product.id)


    def GetProductsByManufacturer(self, request, context):
        manufacturer = request.manufacturer
        for product in inventory.products_by_id.values():
            if product.manufacturer == manufacturer:
                yield init_product(product)


    def GetProductsInStock(self, request, context):
        for product in inventory.products_by_id.values():
            if product.amount > 0:
                yield init_product(product)


    def UpdateProductDescription(self, request, context):
        product_identifier = request.product_identifier
        name = product_identifier.name
        id_ = product_identifier.id
        description = request.description
        if update_description(name, id_, description, inventory):
            return inventory_system_pb2.Success(success = True)
        return inventory_system_pb2.Success(success = False)


    def UpdateProductManufacturer(self, request, context):
        product_identifier = request.product_identifier
        name = product_identifier.name
        id_ = product_identifier.id
        manufacturer = request.manufacturer
        if update_manufacturer(name, id_, manufacturer, inventory):
            return inventory_system_pb2.Success(success = True)
        return inventory_system_pb2.Success(success = False)


    def UpdateProductSaleCost(self, request, context):
        product_identifier = request.product_identifier
        name = product_identifier.name
        id_ = product_identifier.id
        sale_cost = request.sale_cost
        if update_sale_cost(name, id_, sale_cost, inventory):
            return inventory_system_pb2.Success(success = True)
        return inventory_system_pb2.Success(success = False)


    def UpdateProductWholesaleCost(self, request, context):
        product_identifier = request.product_identifier
        name = product_identifier.name
        id_ = product_identifier.id
        wholesale_cost = request.wholesale_cost
        if update_wholesale_cost(name, id_, wholesale_cost, inventory):
            return inventory_system_pb2.Success(success = True)
        return inventory_system_pb2.Success(success = False)


    def IncreaseProductAmount(self, request, context):
        product_identifier = request.product_identifier
        name = product_identifier.name
        id_ = product_identifier.id
        amount = request.amount
        if increase_product_amount(name, id_, amount, inventory):
            return inventory_system_pb2.Success(success = True)
        return inventory_system_pb2.Success(success = False)


    def DecreaseProductAmount(self, request, context):
        product_identifier = request.product_identifier
        name = product_identifier.name
        id_ = product_identifier.id
        amount = request.amount
        if decrease_product_amount(name, id_, amount, inventory):
            return inventory_system_pb2.Success(success = True)
        return inventory_system_pb2.Success(success = False)


    def AddOrder(self, request, context):
        order_id = add_order(retrieve_order(request), inventory)
        return inventory_system_pb2.OrderID(id = order_id)


    def GetOrder(self, request, context):
        id_ = request.id
        if is_order(id_, inventory):
            return init_order(get_order(id_, inventory))
        else:
            return self.null_order


class Inventory:

    def __init__(self):
        self.products_by_id = {}
        self.products_by_name= {}
        self.orders = {}




inventory = Inventory()

def main():
    try:
        global inventory
        if os.path.exists("products.txt"):
            products = open("products.txt", "rb")
            inventory = pickle.load(products)
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        inventory_system_pb2_grpc.add_InventorySystemServicer_to_server(InventorySystem(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()
    except KeyboardInterrupt:
        products = open("products.txt", "wb")
        pickle.dump(inventory, products)
        products.close()


if __name__ == '__main__':
    main()