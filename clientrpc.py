import xmlrpc.client
import pickle
import datetime

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

"""

ids = []
for i in list(range(100)):
    name = "product" + str(i)
    ids = proxy.lookup_by_name(name)

print(ids)"""



"""
ids = []
for i in list(range(200)):
    name = "product" + str(i)
    ids = proxy.add_product(name, "a product", name, 10, 10, 20)
"""

"""
summ = proxy.list_products_by_manufacturer("product150")
print(summ)
"""
