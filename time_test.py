from xmlrpc.client import ServerProxy
import grpc
import time
import argparse
import inventory_system_pb2
import inventory_system_pb2_grpc

AMOUNT_TO_TEST = 100

def run_add_product_grpc(stub):
    for i in range(0, AMOUNT_TO_TEST):
        stub.AddProduct(inventory_system_pb2.Product(name="Product" + str(i + 2000), amount = 0, description = "", manufacturer = "", sale_cost = 0, wholesale_cost = 0))
def run_get_product_grpc(stub):
    for i in range(0, AMOUNT_TO_TEST):
        stub.GetProduct(inventory_system_pb2.ProductIdentifier(name="Product" + str(i), id="-1"))
def run_get_product_manufacturer_grpc(stub):
    stub.GetProductsByManufacturer(inventory_system_pb2.Manufacturer(manufacturer="Google"))
def run_get_product_stock_grpc(stub):
    stub.GetProductsInStock(inventory_system_pb2.Empty())
def run_update_description_grpc(stub):
    for i in range(0, AMOUNT_TO_TEST):
        stub.UpdateProductDescription(inventory_system_pb2.ProductDescription(
                        product_identifier=inventory_system_pb2.ProductIdentifier(name="Product" + str(i), id="-1"),
                        description="updated"))
def run_update_manufacturer_grpc(stub):
    for i in range(0, AMOUNT_TO_TEST):
        stub.UpdateProductManufacturer(inventory_system_pb2.ProductManufacturer(
                        product_identifier=inventory_system_pb2.ProductIdentifier(name="Product" + str(i), id="-1"),
                        manufacturer="updated"))
def run_update_wholesale_grpc(stub):
    for i in range(0, AMOUNT_TO_TEST):
        stub.UpdateProductWholesaleCost(inventory_system_pb2.ProductWholesaleCost(
                        product_identifier=inventory_system_pb2.ProductIdentifier(name="Product" + str(i), id="-1"),
                        wholesale_cost=99))
def run_update_sale_grpc(stub):
    for i in range(0, AMOUNT_TO_TEST):
        stub.UpdateProductSaleCost(inventory_system_pb2.ProductSaleCost(
                        product_identifier=inventory_system_pb2.ProductIdentifier(name="Product" + str(i), id="-1"),
                        sale_cost=99))
def run_increase_grpc(stub):
    for i in range(0, AMOUNT_TO_TEST):
        stub.IncreaseProductAmount(inventory_system_pb2.ProductAmount(
                        product_identifier=inventory_system_pb2.ProductIdentifier(name="Product" + str(i), id="-1"),
                        amount = 10))
def run_decrease_grpc(stub):
    for i in range(0, AMOUNT_TO_TEST):
        stub.DecreaseProductAmount(inventory_system_pb2.ProductAmount(
                        product_identifier=inventory_system_pb2.ProductIdentifier(name="Product" + str(i), id="-1"),
                        amount = 10))
def run_add_order_grpc(stub):
    for i in range(0, AMOUNT_TO_TEST):
        order = inventory_system_pb2.Order(destination="test", date="test", products=[],
                                                   is_paid=False, is_shipped=False)
        stub.AddOrder(order)

def run_get_order_grpc(stub):
    for i in range(0, AMOUNT_TO_TEST):
        stub.GetOrder(inventory_system_pb2.OrderID(id="f76e7160-bdcd-415e-bc95-8625f698da6d"))

def add_product_to_order_grpc(stub):
    for i in range(0, AMOUNT_TO_TEST):
        product_amt = inventory_system_pb2.ProductAmount(
                product_identifier=inventory_system_pb2.ProductIdentifier(name="Product" + str(i), id="-1"),
                amount=20)
        response = stub.AddProductToOrder(
                inventory_system_pb2.OrderProduct(id="f76e7160-bdcd-415e-bc95-8625f698da6d", product_amount=product_amt))
def run_remove_product_from_order_grpc(stub):
    for i in range(0, AMOUNT_TO_TEST):
        product_amt = inventory_system_pb2.ProductAmount(
                product_identifier=inventory_system_pb2.ProductIdentifier(name="Product" + str(i), id="-1"),
                amount=20)
        response = stub.RemoveProductFromOrder(
                inventory_system_pb2.OrderProduct(id="f76e7160-bdcd-415e-bc95-8625f698da6d", product_amount=product_amt))
def run_update_order_destination_grpc(stub):
    for i in range(0, AMOUNT_TO_TEST):
        stub.UpdateOrderDestination(
                    inventory_system_pb2.OrderDestination(id="f76e7160-bdcd-415e-bc95-8625f698da6d", destination="test"))
def run_update_order_date_grpc(stub):
    for i in range(0, AMOUNT_TO_TEST):
        stub.UpdateOrderDate(
                    inventory_system_pb2.OrderDate(id="f76e7160-bdcd-415e-bc95-8625f698da6d", date="test"))
def run_update_order_paid_grpc(stub):
    for i in range(0, AMOUNT_TO_TEST):
        stub.UpdateOrderDestination(
                    inventory_system_pb2.OrderPaid(id="f76e7160-bdcd-415e-bc95-8625f698da6d", is_paid = True))
def run_update_order_shipped_grpc(stub):
    for i in range(0, AMOUNT_TO_TEST):
        stub.UpdateOrderShipped(
                    inventory_system_pb2.OrderShipped(id="f76e7160-bdcd-415e-bc95-8625f698da6d", is_shipped = True))
def run_all_unshipped_grpc(stub):
    stub.GetUnshippedOrders(inventory_system_pb2.Empty())
def run_all_unpaid_grpc(stub):
    stub.GetUnpaidOrders(inventory_system_pb2.Empty())

def main():
    with grpc.insecure_channel("34.226.207.102:25555") as channel:
        total = 0
        stub = inventory_system_pb2_grpc.InventorySystemStub(channel)
        start = time.monotonic()
        run_add_product_grpc(stub)
        end = time.monotonic()
        print("Add: ", end - start)
        total += (end - start)
        start = time.monotonic()
        run_get_product_grpc(stub)
        end = time.monotonic()
        print("Get: ", end - start)
        total += (end - start)
        start = time.monotonic()
        run_get_product_manufacturer_grpc(stub)
        end = time.monotonic()
        print("Get manu: ", end - start)
        total += (end - start)
        start = time.monotonic()
        run_get_product_stock_grpc(stub)
        end = time.monotonic()
        print("Get stock: ", end - start)
        total += (end - start)
        start = time.monotonic()
        run_update_description_grpc(stub)
        end = time.monotonic()
        print("Desc: ", end - start)
        total += (end - start)
        start = time.monotonic()
        run_update_manufacturer_grpc(stub)
        end = time.monotonic()
        print("Manu: ", end - start)
        total += (end - start)
        start = time.monotonic()
        run_update_sale_grpc(stub)
        end = time.monotonic()
        print("Sale: ", end - start)
        total += (end - start)
        start = time.monotonic()
        run_update_wholesale_grpc(stub)
        end = time.monotonic()
        print("Wholesale: ", end - start)
        total += (end - start)
        start = time.monotonic()
        run_increase_grpc(stub)
        end = time.monotonic()
        print("Inc: ", end - start)
        total += (end - start)
        start = time.monotonic()
        run_decrease_grpc(stub)
        end = time.monotonic()
        print("Dec: ", end - start)
        total += (end - start)
        start = time.monotonic()
        run_add_order_grpc(stub)
        end = time.monotonic()
        print("Add order: ", end - start)
        total += (end - start)
        start = time.monotonic()
        run_get_order_grpc(stub)
        end = time.monotonic()
        print("Get order: ", end - start)
        total += (end - start)
        start = time.monotonic()
        add_product_to_order_grpc(stub)
        end = time.monotonic()
        print("Add prod to order: ", end - start)
        total += (end - start)
        start = time.monotonic()
        run_remove_product_from_order_grpc(stub)
        end = time.monotonic()
        print("Remove prod from order: ", end - start)
        total += (end - start)
        start = time.monotonic()
        run_update_order_date_grpc(stub)
        end = time.monotonic()
        print("Date: ", end - start)
        total += (end - start)
        start = time.monotonic()
        run_update_order_destination_grpc(stub)
        end = time.monotonic()
        print("Dest: ", end - start)
        total += (end - start)
        start = time.monotonic()
        run_update_order_paid_grpc(stub)
        end = time.monotonic()
        print("Paid: ", end - start)
        total += (end - start)
        start = time.monotonic()
        run_update_order_shipped_grpc(stub)
        end = time.monotonic()
        print("Shipped: ", end - start)
        total += (end - start)
        start = time.monotonic()
        run_all_unshipped_grpc(stub)
        end = time.monotonic()
        print("All unshipped: ", end - start)
        total += (end - start)
        start = time.monotonic()
        run_all_unpaid_grpc(stub)
        end = time.monotonic()
        print("All unpaid: ", end - start)
        print("Total time: ", total)

if __name__ == "__main__":
    main()