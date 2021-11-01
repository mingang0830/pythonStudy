import sqlite3


class Product:
    def __init__(self, id, name, price, store):
        self.id = id
        self.name = name
        self.price = price
        self.store = store

    def __repr__(self):
        return f'({self.name} - {self.price}원 )'


class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.products = {}
        self.check_stock = {}

    def buy(self, product, amount):
        self.products[product.id] = product
        self.check_stock[product] = amount

    def get_product_id_by_name(self, name):
        for id in self.products:
            if self.products[id].name == name:
                return id

    def out_of_stock(self):
        out_of_stock_items = []
        for product, stock in self.check_stock.items():
            if stock == 0:
                out_of_stock_items.append(product)
        return out_of_stock_items

    def __repr__(self):
        return self.store_name


class Customer:
    def __init__(self):
        self.purchase_list = []

    def buy(self, store, name, amount):
        product_id = store.get_product_id_by_name(name)
        product = store.products[product_id]
        new_amount = store.check_stock[product] - amount
        if new_amount >= 0:
            store.check_stock[product] = new_amount
            self.purchase_list.append({'store': store, 'product': product, 'amount': amount})
            print(f'{product.name} - {amount}개 구매완료!')
        else:
            raise Exception('상품의 재고가 부족합니다.')


if __name__ == "__main__":

    s1 = Store('문구점')
    c1 = Customer()

    for id, name, price, store, amount in [(1,'연필', 1000, s1, 4),
                                              (2, '샤프', 1000, s1, 3),
                                              (3, '지우개', 1000, s1, 2),
                                              (4, '화이트', 1000, s1, 2),
                                              ]:
        s1.buy(Product(id, name, price, store), amount)

    print(s1.products)
    print(s1.get_product_id_by_name('연필'))

    c1.buy(s1, '연필', 3)
    c1.buy(s1, '샤프', 3)
    c1.buy(s1, '지우개', 2)

    print(c1.purchase_list)
    print(s1.check_stock)
    print(s1.out_of_stock())




