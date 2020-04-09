import inventory_system_pb2
import inventory_system_pb2_grpc
import pickle
import os
from inventory_util import Inventory
from concurrent import futures
import grpc
from inventory_system import InventorySystem

def main():
    try:
        if os.path.exists("products.pickle"):
            products = open("products.pickle", "rb")
            inventory = pickle.load(products)
        else:
            inventory = Inventory()
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        inventory_system_pb2_grpc.add_InventorySystemServicer_to_server(InventorySystem(inventory), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()
    except KeyboardInterrupt:
        products = open("products.pickle", "wb")
        pickle.dump(inventory, products)
        products.close()


if __name__ == '__main__':
    main()