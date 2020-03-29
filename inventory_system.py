import grpc
import inventory_system_pb2
import inventory_system_pb2_grpc
from uuid import uuid4
from concurrent import futures




class InventorySystem(inventory_system_pb2_grpc.InventorySystemServicer):

    products = []
    orders = []
    null_product = inventory_system_pb2.Product(name = "null", id = "-1", amount = -1, description = "null", manufacturer = "null",
                sale_cost = 0, wholesale_cost = 0)
    null_identifier = inventory_system_pb2.ProductIdentifier(name = "null", id = "-1")
    null_order = inventory_system_pb2.Order(id = "-1", destination = "N/A", date = "1/1/1970", products = [], is_paid = False, is_shipped = False)

    def GetProduct(self, request, context):
        name = request.name
        id = request.id
        for product in self.products:
            if product.name == name or product.id == id:
                return init_product(product)
        return self.null_product

    def AddProduct(self, request, context):
        new_product = retrieve_product(request)
        for product in self.products:
            if new_product.name == product.name:
                return self.null_identifier
        self.products.append(new_product)
        return inventory_system_pb2.ProductIdentifier(name = new_product.name, id = new_product.id)

    def GetProductsByManufacturer(self, request, context):
        manufacturer = request.manufacturer
        for product in self.products:
            if product.manufacturer == manufacturer:
                yield init_product(product)

    def GetProductsInStock(self, request, context):
        for product in self.products:
            if product.amount > 0:
                yield init_product(product)

    def UpdateProductDescription(self, request, context):
        product_identifier = request.product_identifier
        name = product_identifier.name
        id_ = product_identifier.id
        description = request.description
        for product in self.products:
            if product.name == name or product.id == id_:
                product.description = description
                return inventory_system_pb2.Success(success = True)
        return inventory_system_pb2.Success(success = False)

    def UpdateProductManufacturer(self, request, context):
        product_identifier = request.product_identifier
        name = product_identifier.name
        id_ = product_identifier.id
        manufacturer = request.manufacturer
        for product in self.products:
            if product.name == name or product.id == id_:
                product.manufacturer = manufacturer
                return inventory_system_pb2.Success(success = True)
        return inventory_system_pb2.Success(success = False)

    def UpdateProductSaleCost(self, request, context):
        product_identifier = request.product_identifier
        name = product_identifier.name
        id_ = product_identifier.id
        sale_cost = request.sale_cost
        for product in self.products:
            if product.name == name or product.id == id_:
                product.sale_cost = sale_cost
                return inventory_system_pb2.Success(success = True)
        return inventory_system_pb2.Success(success = False)

    def UpdateProductWholesaleCost(self, request, context):
        product_identifier = request.product_identifier
        name = product_identifier.name
        id_ = product_identifier.id
        wholesale_cost = request.wholesale_cost
        for product in self.products:
            if product.name == name or product.id == id_:
                product.wholesale_cost = wholesale_cost
                return inventory_system_pb2.Success(success = True)
        return inventory_system_pb2.Success(success = False)

    def IncreaseProductAmount(self, request, context):
        product_identifier = request.product_identifier
        name = product_identifier.name
        id_ = product_identifier.id
        amount = request.amount
        for product in self.products:
            if product.name == name or product.id == id_:
                product.amount +=amount
                return inventory_system_pb2.Success(success = True)
        return inventory_system_pb2.Success(success = False)

    def DecreaseProductAmount(self, request, context):
        product_identifier = request.product_identifier
        name = product_identifier.name
        id_ = product_identifier.id
        amount = request.amount
        for product in self.products:
            if product.name == name or product.id == id_:
                if product.amount - amount >= 0:
                    product.amount -= amount
                    return inventory_system_pb2.Success(success = True)
                else:
                    return inventory_system_pb2.Success(success = False)
        return inventory_system_pb2.Success(success = False)

    def AddOrder(self, request, context):
        order = retrieve_order(request)
        valid_products = []
        for order_product in order.products:
            name = order_product.product_identifier.name
            id_ = order_product.product_identifier.id
            for existing_product in self.products:
                if existing_product.name == name or existing_product.id == id_:
                    if existing_product.amount >= order_product.amount:
                        valid_products.append(order_product)
                        existing_product.amount -= order_product.amount
        order.products = valid_products
        self.orders.append(order)
        return inventory_system_pb2.OrderID(id = order.id)

    def GetOrder(self, request, context):
        id_ = request.id
        for order in self.orders:
            if order.id == id_:
                return init_order(order)
        return self.null_order



class Product:

    def __init__(self, name, amount, description, manufacturer, sale_cost, wholesale_cost):
        self.name = name
        self.id = str(uuid4())
        self.amount = amount
        self.description = description
        self.manufacturer = manufacturer
        self.sale_cost = sale_cost
        self.wholesale_cost = wholesale_cost

class Order:

    def __init__(self, destination, date, products, is_paid, is_shipped):
        self.id = str(uuid4())
        self.destination = destination
        self.date = date
        self.products = products
        self.is_paid = is_paid
        self.is_shipped = is_shipped

def init_product(product):
    return inventory_system_pb2.Product(name = product.name, id = product.id, amount = product.amount, description = product.description, manufacturer = product.manufacturer,
                sale_cost = product.sale_cost, wholesale_cost = product.wholesale_cost)

def init_order(order):
    return inventory_system_pb2.Order(id = order.id, destination = order.destination, date = order.date, products=order.products,
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


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_system_pb2_grpc.add_InventorySystemServicer_to_server(InventorySystem(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    main()