import sqlite3

conn = sqlite3.connect('store_sys.db')
cur = conn.cursor()


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
        self.store_name = store_name[1]
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

    stationery_store = cur.execute("select * from store where id=1").fetchone()
    s1 = Store(stationery_store)
    c1 = Customer()

    # product에 물품 추가
    cur.execute("INSERT INTO product Values(5, '마카', 2000);")
    cur.execute("INSERT INTO stock Values(5, 1, 5);")

    # product에서 물건 가져오기
    pencil = cur.execute("select * from product where id=1").fetchone()
    sharp = cur.execute("select * from product where id=2").fetchone()
    eraser = cur.execute("select * from product where id=3").fetchone()
    white = cur.execute("select * from product where id=4").fetchone()
    mark = cur.execute("select * from product where id=5").fetchone()

    for id, name, price in [pencil,
                            sharp,
                            eraser,
                            white,
                            mark]:
        s1.buy(Product(id, name, price, s1), 4)

    print(s1.products)
    print(s1.get_product_id_by_name('마카'))

    c1.buy(s1, '연필', 4)
    c1.buy(s1, '샤프', 3)
    c1.buy(s1, '지우개', 2)

    print(c1.purchase_list)
    print(s1.check_stock)
    print(s1.out_of_stock())

    # print([row for row in cur.execute("select * from product")])

