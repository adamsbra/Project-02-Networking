import grpc
import inventory_system_pb2
import inventory_system_pb2_grpc

def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = inventory_system_pb2_grpc.InventorySystemStub(channel)
        # Add 4 Products initially to test AddProduct method
        response = stub.AddProduct(inventory_system_pb2.Product(name = "Product 1", amount = 0, description="Test Product", manufacturer="Google", sale_cost = 4.2, wholesale_cost = 1.5))
        print(response)
        response = stub.AddProduct(inventory_system_pb2.Product(name = "Product 2", amount = 2, description="Test Product", manufacturer="Amazon", sale_cost = 4.2, wholesale_cost = 1.5))
        print(response)
        response = stub.AddProduct(inventory_system_pb2.Product(name = "Product 3", amount = 0, description="Test Product", manufacturer="Google", sale_cost = 4.2, wholesale_cost = 1.5))
        print(response)
        response = stub.AddProduct(inventory_system_pb2.Product(name = "Product 4", amount = 2, description="Test Product", manufacturer="Best Buy", sale_cost = 4.2, wholesale_cost = 1.5))
        print(response)
        # Get a product to test GetProduct
        response = stub.GetProduct(inventory_system_pb2.ProductIdentifier(name = "Product 1", id = "-1"))
        print(response)
        # Get products by a manufacturer to test GetProductsByManufacturer
        response = stub.GetProductsByManufacturer(inventory_system_pb2.Manufacturer(manufacturer = "Google"))
        for i in response:
            print(i)
        # Get products that are in stock to test GetProductsInStock
        response = stub.GetProductsInStock(inventory_system_pb2.Empty())
        for i in response:
            print(i)
        # Update a product to test UpdateProduct
        response = stub.UpdateProduct(inventory_system_pb2.Product(name="Product 4", amount = 10, description="Test Product Changed", manufacturer="Googler", sale_cost = 50.2, wholesale_cost = 25.1))
        print(response)
        # Get a product to confirm test of UpdateProduct
        response = stub.GetProduct(inventory_system_pb2.ProductIdentifier(name="Product 4", id = "-1"))
        print(response)
if __name__=="__main__":
    main()
