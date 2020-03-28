import xmlrpc.client
import pickle
import datetime

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")


def test_lookup_product_by_name(name):
    ids = proxy.lookup_product_by_name(name)
    print(ids)


def test_add_product():
    id_names = []
    for i in list(range(200)):
        name = "product" + str(i)
        id_names = proxy.add_product(name, "a product", name, 100, 100, 200)
    print(id_names)


def test_list_products_by_manufacturer():
    summ = proxy.list_products_by_manufacturer("product150")
    print(summ)


def test_lower_amount(name, amount):
    success = proxy.lower_amount(name, amount)
    print(success)


def test_increase_amount(name, amount):
    success = proxy.increase_amount(name, amount)
    print(success)


def test_change_manufacturer(name_or_id, manu):
    success = proxy.change_manufacturer(name_or_id, manu)
    print(success)


def test_change_wholesale_cost(name_or_id, wholesale_cost):
    success = proxy.change_wholesale_cost(name_or_id, wholesale_cost)
    print(success)


def test_change_sale_cost(name_or_id, wholesale_cost):
    success = proxy.change_sale_cost(name_or_id, wholesale_cost)
    print(success)


def test_add_order(products_name_or_id, amounts, destination):
    success = proxy.add_order(products_name_or_id, amounts, destination)
    print(success)


def test_list_unshipped():
    success = proxy.list_unshipped()
    print(success)


test_list_unshipped()
