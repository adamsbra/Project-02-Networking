from xmlrpc.server import SimpleXMLRPCServer
import pickle

class product:
    def __init__(self, name, id, amount):
        self.name = name
        self.id = id
        self.amount = amount

    def change_inventory(self, amount):
        self.amount += amount

products = open("products.txt", "rb")
list_of_products = pickle.load(products)
products.close()




def add_product(Product_name, id_, amount):
    if id_ not in list_of_products.keys():
        list_of_products[id_] = product(Product_name, id_, amount)
        return 1
    else:
        return increase_inventory(id_, amount)

def increase_inventory(id, amount):
    if id in list_of_products.keys():
        list_of_products.get(id).change_inventory(amount)
        return 1
    else:
        return -1

def decrease_inventory(id, amount):
    if id in list_of_products.keys():
        if amount <= list_of_products.get(id).amount:
            list_of_products.get(id).change_inventory(-amount)
            return 1
        else:
            return -2
    else:
        return -1

def list_products():
    summary = []
    for id in list_of_products.keys():
        name = list_of_products.get(id).name
        amount = list_of_products.get(id).amount
        summary.append("{0}: {1} units".format(name, amount))
    return summary



#def listProductsWithFilter():



try:
    server = SimpleXMLRPCServer(("localhost", 8000))
    print("Listening on port 8000...")
    server.register_function(add_product, "add_product")
    server.register_function(decrease_inventory, "decrease_inventory")
    server.register_function(increase_inventory, "increase_inventory")
    server.register_function(list_products, "list_products")
    #server.register_function(listProductsWithFilter, "List of products in the inventory wit a filter")
    server.serve_forever()
except KeyboardInterrupt:
    products = open("products.txt", "wb")
    pickle.dump(list_of_products, products)
    products.close()


