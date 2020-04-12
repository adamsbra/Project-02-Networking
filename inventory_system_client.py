import xmlrpc

import grpc
import argparse
import inventory_system_pb2
import inventory_system_pb2_grpc


def str_to_bool(string):
    """
    Taken from stack overflow at
    stackoverflow.com/questions/15008758/parsing-boolean-values-with-argparse
    """
    if isinstance(string, bool):
        return string
    if string.lower() in ('yes', 'true', 't', 'y', 1):
        return True
    elif string.lower() in ('no', 'false', 'f', 'n', 0):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--protocol', type=str, help="Protocol of using gRPC or XML-RPC", default="gRPC")

    subparsers = parser.add_subparsers(title="command", dest="cmd", required=True)

    get_product_cmd = subparsers.add_parser(name="get_product", description="Get a product from the database")
    get_product_cmd.add_argument("--name", help="The name of the product", type=str, default="null", required=False)
    get_product_cmd.add_argument("--id", help="The id of the product", type=str, default="-1", required=False)

    add_product_cmd = subparsers.add_parser(name="add_product", description="Add a product to the database")
    add_product_cmd.add_argument("name", help="The name of the product", type=str)
    add_product_cmd.add_argument("amount", help="The amount of the product", type=int)
    add_product_cmd.add_argument("description", help="The description of the product", type=str)
    add_product_cmd.add_argument("manufacturer", help="The manufacturer of the product", type=str)
    add_product_cmd.add_argument("sale_cost", help="The sale cost of the product", type=float)
    add_product_cmd.add_argument("wholesale_cost", help="The wholesale cost of the product", type=float)

    get_products_by_manufacturer_cmd = subparsers.add_parser(name="get_products_by_manufacturer",
                                                             description="Get a list of products by manufacturer")
    get_products_by_manufacturer_cmd.add_argument("manufacturer", help="The manufacturer you want to filter by")

    get_products_in_stock_cmd = subparsers.add_parser(name="get_products_in_stock",
                                                      description="Get a list of products in stock")

    update_product_description_cmd = subparsers.add_parser(name="update_product_description",
                                                           description="Update the description of a product")
    update_product_description_cmd.add_argument("description", help="The description you want to update to", type=str)
    update_product_description_cmd.add_argument("--name", help="The name of the product", default="null", type=str,
                                                required=False)
    update_product_description_cmd.add_argument("--id", help="The id of the product", default="-1", type=str,
                                                required=False)

    update_product_manufacturer_cmd = subparsers.add_parser(name="update_product_manufacturer",
                                                            description="Update the manufacturer of a product")
    update_product_manufacturer_cmd.add_argument("manufacturer", help="The manufacturer you want to update to",
                                                 type=str)
    update_product_manufacturer_cmd.add_argument("--name", help="The name of the product", type=str, required=False)
    update_product_manufacturer_cmd.add_argument("--id", help="The id of the product", type=str, required=False)

    update_product_wholesalecost_cmd = subparsers.add_parser(name="update_product_wholesalecost",
                                                             description="Update the wholesale cost of a product")
    update_product_wholesalecost_cmd.add_argument("wholesale_cost", help="The price of whole sale cost", type=float)
    update_product_wholesalecost_cmd.add_argument("--name", help="The name of the product", type=str, required=False)
    update_product_wholesalecost_cmd.add_argument("--id", help="The id of the product", type=str, required=False)

    update_product_salecost_cmd = subparsers.add_parser("update_product_salecost",
                                                        description="Update the sale cost of a product")
    update_product_salecost_cmd.add_argument("sale_cost", help="The price of sale cost", type=float)
    update_product_salecost_cmd.add_argument("--name", help="The name of the product", type=str, required=False)
    update_product_salecost_cmd.add_argument("--id", help="The id of the product", type=str, required=False)

    increase_product_amount_cmd = subparsers.add_parser(name="increase_product_amount",
                                                        description="Increase the amount of a product's stock")
    increase_product_amount_cmd.add_argument("amount", help="Amount you want to increase stock by", type=int)
    increase_product_amount_cmd.add_argument("--name", help="The name of the product", type=str, required=False)
    increase_product_amount_cmd.add_argument("--id", help="The id of the product", type=str)

    decrease_product_amount_cmd = subparsers.add_parser(name="decrease_product_amount",
                                                        description="Decrease the amount of a proudct's stock")
    decrease_product_amount_cmd.add_argument("amount", help="Amount you want to decrease stock by", type=int)
    decrease_product_amount_cmd.add_argument("--name", help="The name of the product", type=str, required=False)
    decrease_product_amount_cmd.add_argument("--id", help="The id of the product", type=str, required=False)

    add_order_cmd = subparsers.add_parser(name="add_order", description="Add an order to the database")
    add_order_cmd.add_argument("destination", help="The destination of the order")
    add_order_cmd.add_argument("date", help="The date on which the order was placed.")
    add_order_cmd.add_argument("--products", help="The products that should be added to the order.")

    get_order_cmd = subparsers.add_parser(name="get_order", description="Get an order from the database")
    get_order_cmd.add_argument("id", help="The id of the order", type=str)

    add_product_to_order_cmd = subparsers.add_parser(name="add_product_to_order",
                                                     description="Add a product to an order")
    add_product_to_order_cmd.add_argument("id", help="The id of the order", type=str)
    add_product_to_order_cmd.add_argument("product",
                                          help="The product you want to add,, in the form of \"id, name ,amount\"",
                                          type=str)

    remove_product_from_order_cmd = subparsers.add_parser(name="remove_product_from_order",
                                                          description="Remove a product from an order")
    remove_product_from_order_cmd.add_argument("id", help="The id of the order", type=str)
    remove_product_from_order_cmd.add_argument("product",
                                               help="The product you want to remove, in the form of \"id, name ,amount\"",
                                               type=str)

    update_order_destination_cmd = subparsers.add_parser(name="update_order_destination",
                                                         description="Update the destination of an order")
    update_order_destination_cmd.add_argument("id", help="The id of the order", type=str)
    update_order_destination_cmd.add_argument("destination", help="The new destination of the order")

    update_order_date_cmd = subparsers.add_parser(name="update_order_date", description="Update the date of an order")
    update_order_date_cmd.add_argument("id", help="The id of the order", type=str)
    update_order_date_cmd.add_argument("date", help="The new date of the order")

    update_order_paid_cmd = subparsers.add_parser(name="update_order_paid",
                                                  description="Update if an order is paid or not")
    update_order_paid_cmd.add_argument("id", help="The id of the order", type=str)
    update_order_paid_cmd.add_argument("is_paid", help="Whether or not the order is paid for", nargs='?',
                                       type=str_to_bool, const=True)

    update_order_shipped_cmd = subparsers.add_parser(name="update_order_shipped",
                                                     description="Update if an order has been shipped")
    update_order_shipped_cmd.add_argument("id", help="The id of the order", type=str)
    update_order_shipped_cmd.add_argument("is_shipped", help="Whether or not the order is shipped", nargs='?',
                                          type=str_to_bool, const=True)

    get_unshipped_orders_cmd = subparsers.add_parser(name="get_unshipped_orders",
                                                     description="Get all unshipped orders")

    get_unpaid_orders_cmd = subparsers.add_parser(name="get_unpaid_orders", description="Get all unpaid orders")

    args = parser.parse_args()
    if args.protocol == "gRPC":
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = inventory_system_pb2_grpc.InventorySystemStub(channel)
            if args.cmd == "get_product":
                response = stub.GetProduct(inventory_system_pb2.ProductIdentifier(name=args.name, id=args.id))
                if response.id == -1:
                    print("Failed to get a product by that identifier.")
                else:
                    print(response)
            elif args.cmd == "add_product":
                response = stub.AddProduct(
                    inventory_system_pb2.Product(name=args.name, amount=args.amount, description=args.description,
                                                 manufacturer=args.manufacturer, sale_cost=args.sale_cost,
                                                 wholesale_cost=args.wholesale_cost))
                if response.product_identifier.id == -1:
                    print("Failed to add the product.")
                else:
                    print(response)
            elif args.cmd == "get_products_by_manufacturer":
                response = stub.GetProductsByManufacturer(
                    inventory_system_pb2.Manufacturer(manufacturer=args.manufacturer))
                for i in response:
                    if (i.id == "-1"):
                        print("There are no products by that manufacturer.")
                        break
                    print(i)
            elif args.cmd == "get_products_in_stock":
                response = stub.GetProductsInStock(inventory_system_pb2.Empty())
                for i in response:
                    if (i.id == "-1"):
                        print("There are no products in stock.")
                        break
                    print(i)
            elif args.cmd == "update_product_description":
                response = stub.UpdateProductDescription(inventory_system_pb2.ProductDescription(
                    product_identifier=inventory_system_pb2.ProductIdentifier(name=args.name, id=args.id),
                    description=args.description))
                if response.success:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "update_product_manufacturer":
                response = stub.UpdateProductManufacturer(inventory_system_pb2.ProductManufacturer(
                    product_identifier=inventory_system_pb2.ProductIdentifier(name=args.name, id=args.id),
                    manufacturer=args.manufacturer))
                if response.success:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "update_product_wholesalecost":
                response = stub.UpdateProductWholesaleCost(inventory_system_pb2.ProductWholesaleCost(
                    product_identifier=inventory_system_pb2.ProductIdentifier(name=args.name, id=args.id),
                    wholesale_cost=args.wholesale_cost))
                if response.success:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "update_product_salecost":
                response = stub.UpdateProductSaleCost(inventory_system_pb2.ProductSaleCost(
                    product_identifier=inventory_system_pb2.ProductIdentifier(name=args.name, id=args.id),
                    sale_cost=args.sale_cost))
                if response.success:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "increase_product_amount":
                response = stub.IncreaseProductAmount(inventory_system_pb2.ProductAmount(
                    product_identifier=inventory_system_pb2.ProductIdentifier(name=args.name, id=args.id),
                    amount=args.amount))
                if response.success:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "decrease_product_amount":
                response = stub.DecreaseProductAmount(inventory_system_pb2.ProductAmount(
                    product_identifier=inventory_system_pb2.ProductIdentifier(name=args.name, id=args.id),
                    amount=args.amount))
                if response.success:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "add_order":
                order = inventory_system_pb2.Order(destination=args.destination, date=args.date, products=[],
                                                   is_paid=False, is_shipped=False)
                response = stub.AddOrder(order)
                if response.id == -1:
                    print("Failed to add the order")
                else:
                    print(response)
            elif args.cmd == "get_order":
                response = stub.GetOrder(inventory_system_pb2.OrderID(id=args.id))
                if response.id == -1:
                    print("Failed to get an order by that id.")
                else:
                    print(response)
            elif args.cmd == "add_product_to_order":
                product = args.product.split(",")
                product_amt = inventory_system_pb2.ProductAmount(
                    product_identifier=inventory_system_pb2.ProductIdentifier(name=product[0], id=product[1]),
                    amount=int(product[2]))
                response = stub.AddProductToOrder(
                    inventory_system_pb2.OrderProduct(id=args.id, product_amount=product_amt))
                if response.success:
                    print("Added successfully")
                else:
                    print("Failed to add product to order")
            elif args.cmd == "remove_product_from_order":
                product = args.product.split(",")
                product_amt = inventory_system_pb2.ProductAmount(
                    product_identifier=inventory_system_pb2.ProductIdentifier(name=product[0], id=product[1]),
                    amount=int(product[2]))
                response = stub.RemoveProductFromOrder(
                    inventory_system_pb2.OrderProduct(id=args.id, product_amount=product_amt))
                if response.success:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "update_order_destination":
                response = stub.UpdateOrderDestination(
                    inventory_system_pb2.OrderDestination(id=args.id, destination=args.destination))
                if response.success:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "update_order_date":
                response = stub.UpdateOrderDate(inventory_system_pb2.OrderDate(id=args.id, date=args.date))
                if response.success:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "update_order_paid":
                response = stub.UpdateOrderPaid(inventory_system_pb2.OrderPaid(id=args.id, is_paid=args.is_paid))
                if response.success:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "update_order_shipped":
                response = stub.UpdateOrderShipped(
                    inventory_system_pb2.OrderShipped(id=args.id, is_shipped=args.is_shipped))
                if response.success:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "get_unpaid_orders":
                response = stub.GetUnpaidOrders(inventory_system_pb2.Empty())
                for i in response:
                    if (i.id == "-1"):
                        print("There are no unpaid orders.")
                        break
                    print(i)
            elif args.cmd == "get_unshipped_orders":
                response = stub.GetUnshippedOrders(inventory_system_pb2.Empty())
                for i in response:
                    if (i.id == "-1"):
                        print("There are no unshipped orders.")
                        break
                    print(i)
    elif args.cmd == "XML-RPC":
        try:
            proxy = xmlrpc.client.ServerProxy("http://localhost:50051/")
            if args.cmd == "get_product":
                response = proxy.get_product_summary(args.name, args.id)
                if response is not -1:
                    name, id_, description, manufacturer, amount = response
                    new_line = "\n"
                    summary = "Name: {1}{0}ID: {2}{0}Manufacturer: {3}{0}Amount {4}{0}Description: {5}{0}".format(
                        new_line, name, id_, manufacturer, amount, description)
                    print(summary)
                else:
                    print("Product not in inventory")
            elif args.cmd == "get_order":
                response = proxy.get_order_summary(args.id)
                if response is not -1:
                    id_, destination, date, is_shipped, is_paid, products = response
                    new_line = "\n"
                    summary = "ID: {1}{0}ID: {2}{0}Destination: {3}{0}Date {4}{0}shipped: {5}{0}Paid: ".format(
                        new_line, id_, destination, date, is_shipped, is_paid, )
                    for product in products:
                        Name, ID, Amount = product[0], product[1], product[2]
                        print("product Name: {1}{0}ID: {2}{0}Amount: {3}{0}".format(new_line, Name, ID, Amount))
                    print(summary)
            elif args.cmd == "add_product":
                response = proxy.add_product(args.name, args.description, args.manufacturer, args.sale_cost,
                                             args.whole_sale_cost, args.amount)
                if response[1] == -1:
                    print("Failed to get a product by that identifier.")
                else:
                    print(response)
            elif args.cmd == "get_products_by_manufacturer":
                response = proxy.get_products_by_manufacturer(args.manufacturer)
                if response is -1:
                    print("there are not products under that manufacturer")
                else:
                    for i in response:
                        print(i)
            elif args.cmd == "get_products_in_stock":
                response = proxy.list_products
                if response is -1:
                    print("there are no products in the inventory")
                else:
                    for product in response:
                        print(product)
            elif args.cmd == "update_product_description":
                response = proxy.update_description(args.name, args.id, args.description)
                if response:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "update_product_manufacturer":
                response = proxy.update_manufacturer(args.name, args.id, args.manufacturer)
                if response:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "update_product_wholesalecost":
                response = proxy.update_wholesale_cost(args.name, args.id, args.wholesale_cost)
                if response:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "update_product_salecost":
                response = proxy.update_sale_cost(args.name, args.id, args.sale_cost)
                if response:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "increase_product_amount":
                response = proxy.increase_product_amount(args.name, args.id, args.amount)
                if response:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "decrease_product_amount":
                response = proxy.decrease_product_amount(args.name, args.id_, args.amount)
                if response:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "add_order":
                response = proxy.add_order(args.products, args.destination, args.date)
                if response[1] == -1:
                    print("Failed to add the order")
                else:
                    print(response)
            elif args.cmd == "add_product_to_order":
                product = args.product.split(",")
                response = proxy.add_product_to_order(args.id, product[0], product[1], int(product[2]))
                if response:
                    print("Added successfully")
                else:
                    print("Failed to add product to order")
            elif args.cmd == "remove_product_from_order":
                product = args.product.split(",")
                response = proxy.remove_product_from_order(args.id, product[0], product[1], int(product[2]))
                if response:
                    print("Added successfully")
                else:
                    print("Failed to add product to order")
            elif args.cmd == "update_order_destination":
                response = proxy.update_order_destination(args.id, args.destination)
                if response:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "update_order_date":
                response = proxy.update_order_date(args.id, args.date)
                if response:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "update_order_paid":
                response = proxy.update_order_paid(args.id, args.is_paid)
                if response:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "update_order_shipped":
                response = proxy.update_order_shipped(args.id, args.is_shipped)
                if response:
                    print("Updated successfully")
                else:
                    print("Failed to update")
            elif args.cmd == "get_unpaid_orders":
                response = proxy.list_unpaid()
                if response == []:
                    print("There are no orders")
                else:
                    for orderID in response:
                        print(orderID)
            elif args.cmd == "get_unshipped_orders":
                response = proxy.list_unshipped()
                if not response:
                    print("There are no orders")
                else:
                    for orderID in response:
                        print(orderID)



        except KeyboardInterrupt:
            print("Have a good one!")


if __name__ == "__main__":
    main()
