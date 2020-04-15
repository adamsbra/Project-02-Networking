import grpc
import inventory_system_pb2
import inventory_system_pb2_grpc
import pickle
import os
from uuid import uuid4
from concurrent import futures
from inventory_util import *


class InventorySystem(inventory_system_pb2_grpc.InventorySystemServicer):
    # null_product is a product which has all attributes null so that we can tell the client that a product
    # was not found.
    null_product = inventory_system_pb2.Product(name="null", id="-1", amount=-1, description="null",
                                                manufacturer="null",
                                                sale_cost=0, wholesale_cost=0)
    # null_identifier is a product identifier which has all attributes null so that we can tell the client that a product
    # was not found.
    null_identifier = inventory_system_pb2.ProductIdentifier(name="null", id="-1")
    # null_order is an order which has all attributes null so that we can tell the client that an order
    # was not found.
    null_order = inventory_system_pb2.Order(id="-1", destination="N/A", date="1/1/1970", products=[], is_paid=False,
                                            is_shipped=False)

    def __init__(self, inventory):
        self.inventory = inventory

    def GetProduct(self, request, context):
        name = request.name
        id_ = request.id
        if self.inventory.is_product(name, id_):
            return init_product(self.inventory.get_product(name, id_))
        else:
            return self.null_product

    def AddProduct(self, request, context):
        new_product = retrieve_product(request)
        name, id_ = self.inventory.add_product(new_product)
        return inventory_system_pb2.ProductIdentifier(name=name, id=id_)

    def GetProductsByManufacturer(self, request, context):
        """
        This method was done seperate from the helper file due to the yielding of products in gRPC.
        This method searches through the list and yields any products that have a matching manufacturer.
        If no products are ever found, we return a null product
        """
        found_one = False
        manufacturer = request.manufacturer
        for product in self.inventory.products_by_id.values():
            if product.manufacturer == manufacturer:
                found_one = True
                yield init_product(product)
        if not found_one:
            yield self.null_product

    def GetProductsInStock(self, request, context):
        """
        This method is very similar to the previous GetProductsByManufacturer, and not contained in the helper
        file. Searches through all products and returns any that are in stock.
        """
        found_one = False
        for product in self.inventory.products_by_id.values():
            if product.amount > 0:
                found_one = True
                yield init_product(product)
        if not found_one:
            yield self.null_product

    def UpdateProductDescription(self, request, context):
        product_identifier = request.product_identifier
        name = product_identifier.name
        id_ = product_identifier.id
        description = request.description
        if self.inventory.update_description(name, id_, description):
            return inventory_system_pb2.Success(success=True)
        return inventory_system_pb2.Success(success=False)

    def UpdateProductManufacturer(self, request, context):
        product_identifier = request.product_identifier
        name = product_identifier.name
        id_ = product_identifier.id
        manufacturer = request.manufacturer
        if self.inventory.update_manufacturer(name, id_, manufacturer):
            return inventory_system_pb2.Success(success=True)
        return inventory_system_pb2.Success(success=False)

    def UpdateProductSaleCost(self, request, context):
        product_identifier = request.product_identifier
        name = product_identifier.name
        id_ = product_identifier.id
        sale_cost = request.sale_cost
        if self.inventory.update_sale_cost(name, id_, sale_cost):
            return inventory_system_pb2.Success(success=True)
        return inventory_system_pb2.Success(success=False)

    def UpdateProductWholesaleCost(self, request, context):
        product_identifier = request.product_identifier
        name = product_identifier.name
        id_ = product_identifier.id
        wholesale_cost = request.wholesale_cost
        if self.inventory.update_wholesale_cost(name, id_, wholesale_cost):
            return inventory_system_pb2.Success(success=True)
        return inventory_system_pb2.Success(success=False)

    def IncreaseProductAmount(self, request, context):
        product_identifier = request.product_identifier
        name = product_identifier.name
        id_ = product_identifier.id
        amount = request.amount
        if self.inventory.increase_product_amount(name, id_, amount):
            return inventory_system_pb2.Success(success=True)
        return inventory_system_pb2.Success(success=False)

    def DecreaseProductAmount(self, request, context):
        product_identifier = request.product_identifier
        name = product_identifier.name
        id_ = product_identifier.id
        amount = request.amount
        if self.inventory.decrease_product_amount(name, id_, amount):
            return inventory_system_pb2.Success(success=True)
        return inventory_system_pb2.Success(success=False)

    def AddOrder(self, request, context):
        order_id = self.inventory.add_order(retrieve_order(request))
        return inventory_system_pb2.OrderID(id=order_id)

    def GetOrder(self, request, context):
        id_ = request.id
        if self.inventory.is_order(id_):
            return init_order(self.inventory.get_order(id_))
        else:
            return self.null_order

    def AddProductToOrder(self, request, context):
        product_amount = request.product_amount
        product_identifier = product_amount.product_identifier
        product_name = product_identifier.name
        product_id = product_identifier.id
        product_amount = product_amount.amount
        order_id = request.id
        if self.inventory.add_product_to_order(order_id, product_name, product_id, product_amount):
            return inventory_system_pb2.Success(success=True)
        else:
            return inventory_system_pb2.Success(success=False)

    def RemoveProductFromOrder(self, request, context):
        product_amount = request.product_amount
        product_identifier = product_amount.product_identifier
        product_name = product_identifier.name
        product_id = product_identifier.id
        product_amount = product_amount.amount
        order_id = request.id
        if self.inventory.remove_product_from_order(order_id, product_name, product_id, product_amount):
            return inventory_system_pb2.Success(success=True)
        else:
            return inventory_system_pb2.Success(success=False)

    def UpdateOrderDestination(self, request, context):
        order_id = request.id
        destination = request.destination
        if self.inventory.update_order_destination(order_id, destination):
            return inventory_system_pb2.Success(success=True)
        else:
            return inventory_system_pb2.Success(success=False)

    def UpdateOrderDate(self, request, context):
        order_id = request.id
        date = request.date
        if self.inventory.update_order_date(order_id, date):
            return inventory_system_pb2.Success(success=True)
        else:
            return inventory_system_pb2.Success(success=False)

    def UpdateOrderPaid(self, request, context):
        order_id = request.id
        is_paid = request.is_paid
        if self.inventory.update_order_paid(order_id, is_paid):
            return inventory_system_pb2.Success(success=True)
        else:
            return inventory_system_pb2.Success(success=False)

    def UpdateOrderShipped(self, request, context):
        order_id = request.id
        is_shipped = request.is_shipped
        if self.inventory.update_order_shipped(order_id, is_shipped):
            return inventory_system_pb2.Success(success=True)
        else:
            return inventory_system_pb2.Success(success=False)

    def GetUnshippedOrders(self, request, context):
        """
        This method was not included in the helper file as it has different implementation in gRPC.
        Searches through orders finding orders which have not been shipped.
        If none are found, a null order is returned.
        """
        found_one = False
        for order in self.inventory.orders.values():
            if not order.is_shipped:
                found_one = True
                yield init_order(order)
        if not found_one:
            yield self.null_order

    def GetUnpaidOrders(self, request, context):
        """
        Similar to GetUnshippedOrders, returns a null order if none are found
        """
        found_one = False
        for order in self.inventory.orders.values():
            if not order.is_paid:
                found_one = True
                yield init_order(order)
        if not found_one:
            yield self.null_order
