import inventory_system_pb2
import inventory_system_pb2_grpc
import pickle
import os
from inventory_util import Inventory
from concurrent import futures
import grpc
from inventory_system import InventorySystem
from xmlrpc.server import SimpleXMLRPCServer
import XMLRPC

def main():
    try:
        if os.path.exists("products.pickle"):
            try:
                products = open("products.pickle", "rb")
                inventory = pickle.load(products)
            except EOFError:
                inventory = Inventory()
        else:
            inventory = Inventory()
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        inventory_system_pb2_grpc.add_InventorySystemServicer_to_server(InventorySystem(inventory), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        server_xml = SimpleXMLRPCServer(("", 25565))
        XMLRPC.start_xml(server_xml, inventory)
        server.wait_for_termination()
    except KeyboardInterrupt:
        server_xml.shutdown()
        products = open("products.pickle", "wb")
        pickle.dump(inventory, products)
        products.close()


if __name__ == '__main__':
    main()