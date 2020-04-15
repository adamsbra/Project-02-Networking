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
    for i in range(0, AMOUNT_TO_TEST):
        stub.GetProductsByManufacturer(inventory_system_pb2.Manufacturer(manufacturer="Google"))
def run_get_product_stock_grpc(stub):
    for i in range(0, AMOUNT_TO_TEST):
        response = stub.GetProductsInStock(inventory_system_pb2.Empty())
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
    for i in range(0, AMOUNT_TO_TEST):
        stub.GetUnshippedOrders(inventory_system_pb2.Empty())
def run_all_unpaid_grpc(stub):
    for i in range(0, AMOUNT_TO_TEST):
        stub.GetUnpaidOrders(inventory_system_pb2.Empty())

def run_add_product_XML(proxy):
    """Function to test time on the add product functionality of the inventory"""
    for i in range(0, AMOUNT_TO_TEST):
        proxy.add_product("productXML"+str(i), "another Product", "manu", 20,
                          15, 200)
def run_get_product_XML(proxy):
    """Function to test time on the get product functionality of the inventory"""
    for i in range(0, AMOUNT_TO_TEST):
        proxy.get_product_summary("productXML"+str(i), "-1")
def run_get_product_manufacturer_XML(proxy):
    """function to test time on the get products by manufacturer functionality of the inventory"""
    proxy.list_products_by_manufacturer("manu")
def run_get_product_stock_XML(proxy):
    """Function to test time on the list products of the inventory"""
    proxy.list_products()
def run_update_description_XML(proxy):
    """Function to test time on the update product description functionality of the inventory"""
    for i in range(0, AMOUNT_TO_TEST):
        proxy.update_description("productXML"+str(i), "-1", "a new description")
def run_update_manufacturer_XML(proxy):
    """Function to test time on the update manufacturer functionality of the inventory"""
    for i in range(0, AMOUNT_TO_TEST):
        proxy.update_manufacturer("productXML"+str(i), "-1", "Manu2")
def run_update_wholesale_XML(proxy):
    """Function to test time on the update whole sale functionality of the inventory"""
    for i in range(0, AMOUNT_TO_TEST):
        proxy.update_wholesale_cost("productXML"+str(i), "-1", 30)
def run_update_sale_XML(proxy):
    """Function to test time on the update sale cost functionality of the inventory"""
    for i in range(0, AMOUNT_TO_TEST):
        proxy.update_sale_cost("productXML"+str(i), "-1", 20)
def run_increase_XML(proxy):
    """Function to test time on the increase product amount functionality of the inventory"""
    for i in range(0, AMOUNT_TO_TEST):
        proxy.increase_product_amount("productXML"+str(i), "-1", 40)
def run_decrease_XML(proxy):
    """Function to test time on the decrease product amount functionality of the inventory"""
    for i in range(0, AMOUNT_TO_TEST):
        proxy.decrease_product_amount("productXML"+str(i), "-1", 5)
def run_add_order_XML(proxy):
    """Function to test time on the add_order functionality of the inventory"""
    for i in range(0, AMOUNT_TO_TEST):
        proxy.add_order([["-1", "productXML"+str(i), 40]], "somewhere", "Today")
def run_get_order_XML(proxy):
    """Function to test time on the get order functionality of the inventory"""
    for i in range(0, AMOUNT_TO_TEST):
        proxy.get_order_summary("6eab8c15-3d12-43ed-8bc8-63c36718c105")
def add_product_to_order_XML(proxy):
    """Function to test time on the add product to order functionality of the inventory"""
    for i in range(0, AMOUNT_TO_TEST):
        proxy.add_product_to_order("6eab8c15-3d12-43ed-8bc8-63c36718c105", "-1", "productXML"+str(i), 30)
def run_remove_product_from_order_XML(proxy):
    """Function to test time on the remove product from order functionality"""
    for i in range(0, AMOUNT_TO_TEST):
        proxy.remove_product_from_order("6eab8c15-3d12-43ed-8bc8-63c36718c105", "-1", "productXML" + str(i), 5)
def run_update_order_destination_XML(proxy):
    """Function to test time on the update order destination functionality of the inventory"""
    for i in range(0, AMOUNT_TO_TEST):
        proxy.update_order_destination("6eab8c15-3d12-43ed-8bc8-63c36718c105", "destination")
def run_update_order_date_XML(proxy):
    """Function to test time on the update order date functionality of the inventory"""
    for i in range(0, AMOUNT_TO_TEST):
        proxy.update_order_date("6eab8c15-3d12-43ed-8bc8-63c36718c105", "a new date")
def run_update_order_paid_XML(proxy):
    """Function to test time on the update order is paid functionality of the inventory"""
    for i in range(0, AMOUNT_TO_TEST):
        proxy.update_order_paid("6eab8c15-3d12-43ed-8bc8-63c36718c105", "True")
def run_update_order_shipped_XML(proxy):
    """Function to test time on the update order is paid functionality of the inventory"""
    for i in range(0, AMOUNT_TO_TEST):
        proxy.update_order_shipped("6eab8c15-3d12-43ed-8bc8-63c36718c105", "True")
def run_all_unshipped_XML(proxy):
    proxy.list_unpaid()
def run_all_unpaid_XML(proxy):
    proxy.list_unshipped()


list_of_functions = ["run_add_product_XML(proxy)", "run_get_product_XML(proxy)",
                     "run_get_product_manufacturer_XML(proxy)",
                     "run_get_product_stock_XML(proxy)", "run_update_description_XML(proxy)",
                     "run_update_manufacturer_XML(proxy)", "run_update_wholesale_XML(proxy)",
                     "run_update_sale_XML(proxy)", "run_increase_XML(proxy)", "run_decrease_XML(proxy)",
                     "run_get_order_XML(proxy)",
                     "run_update_order_destination_XML(proxy)",
                     "run_update_order_date_XML(proxy)", "run_update_order_paid_XML(proxy)",
                     "run_update_order_shipped_XML(proxy)", "run_all_unshipped_XML(proxy)", "run_all_unpaid_XML(proxy)",
                     "run_add_order_XML(proxy)", "add_product_to_order_XML(proxy)",
                     "run_remove_product_from_order_XML(proxy)"]

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


    total_xml = 0
    # Todo Need to review the add order, add product to order and remove product from order functions
    with ServerProxy("http://34.226.207.102:25565/") as proxy:
        for i in list_of_functions:
            start = time.monotonic()
            eval(i)
            end = time.monotonic()
            print(i+": ", end - start)
            total_xml += (end - start)
        print(total_xml)


if __name__ == "__main__":
    main()