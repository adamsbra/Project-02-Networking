import grpc
import inventory_system_pb2
import inventory_system_pb2_grpc

def main():
    parser = argparse.ArgumentParser()
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = inventory_system_pb2_grpc.InventorySystemStub(channel)
        #Add 4 Products initially to test AddProduct method
        # response = stub.AddProduct(inventory_system_pb2.Product(name = "Product 1", amount = 10, description="Test Product", manufacturer="Google", sale_cost = 4.2, wholesale_cost = 1.5))
        # print(response)
        # response = stub.AddProduct(inventory_system_pb2.Product(name = "Product 2", amount = 23, description="Test Product", manufacturer="Amazon", sale_cost = 4.2, wholesale_cost = 1.5))
        # print(response)
        # response = stub.AddProduct(inventory_system_pb2.Product(name = "Product 3", amount = 50, description="Test Product", manufacturer="Google", sale_cost = 4.2, wholesale_cost = 1.5))
        # print(response)
        # response = stub.AddProduct(inventory_system_pb2.Product(name = "Product 4", amount = 100, description="Test Product", manufacturer="Best Buy", sale_cost = 4.2, wholesale_cost = 1.5))
        # print(response)
        # Get a product to test GetProduct
        # response = stub.GetProduct(inventory_system_pb2.ProductIdentifier(name = "Product 1", id = "-1"))
        # print(response)
        # # # Get products by a manufacturer to test GetProductsByManufacturer
        # response = stub.GetProductsByManufacturer(inventory_system_pb2.Manufacturer(manufacturer = "Google"))
        # for i in response:
        #     print(i)
        # # # Get products that are in stock to test GetProductsInStock
        # response = stub.GetProductsInStock(inventory_system_pb2.Empty())
        # for i in response:
        #     print(i)
        # # # Update a product to test UpdateProductDescription
        # response = stub.UpdateProductDescription(inventory_system_pb2.ProductDescription(product_identifier = inventory_system_pb2.ProductIdentifier(name = "Product 4", id = "-1"), description = "Test Product Changed"))
        # print(response)
        # # # Get a product to confirm test of UpdateProduct
        # response = stub.GetProduct(inventory_system_pb2.ProductIdentifier(name="Product 4", id = "-1"))
        # print(response)

        # response = stub.UpdateProductManufacturer(inventory_system_pb2.ProductManufacturer(product_identifier = inventory_system_pb2.ProductIdentifier(name = "Product 4", id = "-1"), manufacturer = "Manufacturer Changed"))
        # print(response)

        # response = stub.GetProduct(inventory_system_pb2.ProductIdentifier(name="Product 4", id = "-1"))
        # print(response)

        # response = stub.UpdateProductSaleCost(inventory_system_pb2.ProductSaleCost(product_identifier = inventory_system_pb2.ProductIdentifier(name = "Product 4", id = "-1"), sale_cost = 20.00))
        # print(response)

        # response = stub.GetProduct(inventory_system_pb2.ProductIdentifier(name="Product 4", id = "-1"))
        # print(response)

        # response = stub.UpdateProductWholesaleCost(inventory_system_pb2.ProductWholesaleCost(product_identifier = inventory_system_pb2.ProductIdentifier(name = "Product 4", id = "-1"), wholesale_cost = 999.00))
        # print(response)

        # response = stub.GetProduct(inventory_system_pb2.ProductIdentifier(name="Product 4", id = "-1"))
        # print(response)

        # response = stub.IncreaseProductAmount(inventory_system_pb2.ProductAmount(product_identifier = inventory_system_pb2.ProductIdentifier(name = "Product 4", id = "-1"), amount = 100))
        # print(response)

        # response = stub.GetProduct(inventory_system_pb2.ProductIdentifier(name="Product 4", id = "-1"))
        # print(response)

        # response = stub.DecreaseProductAmount(inventory_system_pb2.ProductAmount(product_identifier = inventory_system_pb2.ProductIdentifier(name = "Product 4", id = "-1"), amount = 50))
        # print(response)

        # response = stub.GetProduct(inventory_system_pb2.ProductIdentifier(name="Product 4", id = "-1"))
        # print(response)

        # response = stub.DecreaseProductAmount(inventory_system_pb2.ProductAmount(product_identifier = inventory_system_pb2.ProductIdentifier(name = "Product 4", id = "-1"), amount = 150))
        # print(response)

        # response = stub.UpdateProductWholesaleCost(inventory_system_pb2.ProductWholesaleCost(product_identifier = inventory_system_pb2.ProductIdentifier(name = "Product 999", id = "-1"), wholesale_cost = 999.00))
        # print(response.success)
        # products_add = [(inventory_system_pb2.ProductAmount(product_identifier = inventory_system_pb2.ProductIdentifier(name = "Product 4"), amount = 5))]
        # order = inventory_system_pb2.Order(destination = "My house", date = "Today", products = products_add, is_paid = False, is_shipped =False)
        # response = stub.AddOrder(order)
        # print(response)

        # response = stub.GetOrder(inventory_system_pb2.OrderID(id = "6e7d38e5-2754-4aca-b5c6-30b441fb0c25"))
        # print(response)
        # print(response)
        # response = stub.GetProduct(inventory_system_pb2.ProductIdentifier(name = "Product 4"))
        # print(response)

        # response = stub.RemoveProductFromOrder(inventory_system_pb2.OrderProduct(id = "6e7d38e5-2754-4aca-b5c6-30b441fb0c25", product_amount = inventory_system_pb2.ProductAmount(product_identifier = inventory_system_pb2.ProductIdentifier(name = "Product 4"), amount = 3)))

        # print(response.success)
        # response = stub.GetProduct(inventory_system_pb2.ProductIdentifier(name = "Product 4"))
        # print(response)

        # response = stub.UpdateOrderDestination(inventory_system_pb2.OrderDestination(id = "6e7d38e5-2754-4aca-b5c6-30b441fb0c25", destination = "Changed it ya dummy"))
        # print(response)

        # response = stub.UpdateOrderDate(inventory_system_pb2.OrderDate(id = "6e7d38e5-2754-4aca-b5c6-30b441fb0c25", date = "In like 5 minutes"))
        # print(response)

        # response = stub.UpdateOrderPaid(inventory_system_pb2.OrderPaid(id = "6e7d38e5-2754-4aca-b5c6-30b441fb0c25", is_paid = False))
        # print(response)

        # response = stub.UpdateOrderShipped(inventory_system_pb2.OrderShipped(id = "6e7d38e5-2754-4aca-b5c6-30b441fb0c25", is_shipped = False))
        # print(response)

        # response = stub.GetOrder(inventory_system_pb2.OrderID(id = "6e7d38e5-2754-4aca-b5c6-30b441fb0c25"))
        # print(response)

        # response = stub.GetUnpaidOrders(inventory_system_pb2.Empty())
        # for i in response:
        #     print(i)


if __name__=="__main__":
    main()





