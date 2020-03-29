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
                return inventory_system_pb2.Success(success = False)
        self.products.append(new_product)
        return inventory_system_pb2.Success(success = True)

    def GetProductsByManufacturer(self, request, context):
        manufacturer = request.manufacturer
        for product in self.products:
            if product.manufacturer == manufacturer:
                yield init_product(product)

    def GetProductsInStock(self, request, context):
        for product in self.products:
            if product.amount > 0:
                yield init_product(product)

    def UpdateProduct(self, request, context):
        updated_product = retrieve_product(request)
        for product in self.products:
            if product.name == updated_product.name:
                product.updateProduct(updated_product)
                return inventory_system_pb2.Success(success = True)
        return inventory_system_pb2.Success(success = False)

class Product:

    def __init__(self, name, amount, description, manufacturer, sale_cost, wholesale_cost):
        self.name = name
        self.id = str(uuid4())
        self.amount = amount
        self.description = description
        self.manufacturer = manufacturer
        self.sale_cost = sale_cost
        self.wholesale_cost = wholesale_cost

    def updateProduct(self, product):
        self.amount = product.amount
        self.description = product.description
        self.manufacturer = product.manufacturer
        self.sale_cost = product.sale_cost
        self.wholesale_cost = product.wholesale_cost



def init_product(product):
    return inventory_system_pb2.Product(name = product.name, id = product.id, amount = product.amount, description = product.description, manufacturer = product.manufacturer,
                sale_cost = product.sale_cost, wholesale_cost = product.wholesale_cost)

def retrieve_product(request):
    name = request.name
    amount = request.amount
    description = request.description
    manufacturer = request.manufacturer
    sale_cost = request.sale_cost
    wholesale_cost = request.wholesale_cost
    return Product(name, amount, description, manufacturer, sale_cost, wholesale_cost)

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inventory_system_pb2_grpc.add_InventorySystemServicer_to_server(InventorySystem(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    main()

