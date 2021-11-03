import sqlite3

conn = sqlite3.connect('store_sys.db')
cur = conn.cursor()


class Product:
    def __init__(self, id, name, price):
        cur.execute("insert into product values(?,?,?)", (id, name, price))
        self.id = cur.execute("select id from product where id={}".format(id)).fetchone()[0]
        self.name = cur.execute("select name from product where id={}".format(id)).fetchone()[0]
        self.price = cur.execute("select price from product where id={}".format(id)).fetchone()[0]

    def __repr__(self):
        return f"('{self.name}', {self.price})"


class Store:
    def __init__(self, name):
        cur.execute("insert into store (name) values('{}')".format(name))
        self.id = cur.execute("select id from store where name='{}'".format(name)).fetchone()[0]
        self.name = cur.execute("select name from store where name='{}'".format(name)).fetchone()[0]
        self.check_stock = {}

    def buy(self, product, amount):
        cur.execute("insert into stock (store_id, product_id) values(?,?)", (self.id, product.id))
        self.check_stock[(product.name, product.price)] = amount

    def products(self):
        products = {}
        for product_id in cur.execute("select product_id from stock where store_id={}".format(self.id)).fetchall():
            if product_id == cur.execute("select id from product where id='{}'".format(product_id[0])).fetchone():
                products[product_id[0]] = cur.execute("select name, price from product where id={}".format(product_id[0])).fetchone()
        return products

    def get_product_id_by_name(self, name):
        for product_id in cur.execute("select product_id from stock where store_id={}".format(self.id)).fetchall():
            if product_id == cur.execute("select id from product where name='{}'".format(name)).fetchone():
                return product_id[0]

    def out_of_stock(self):
        out_of_stock_items = []
        for product, stock in self.check_stock.items():
            if stock == 0:
                out_of_stock_items.append(product)
        return out_of_stock_items

    def __repr__(self):
        return f"{self.name}"

class Customer:
    def __init__(self):
        self.purchase_list = []

    def buy(self, store, name, amount):
        product_id = store.get_product_id_by_name(name)
        product = store.products()[product_id]
        new_amount = store.check_stock[product] - amount
        if new_amount >= 0:
            store.check_stock[product] = new_amount
            self.purchase_list.append({'store': store, 'product': product, 'amount': amount})
            print(f'{product} - {amount}개 구매완료!')
        else:
            raise Exception('상품의 재고가 부족합니다.')


if __name__ == "__main__":

    s1 = Store('문방구')
    s2 = Store('문방구2')
    c1 = Customer()
    # print(s1.id)
    # print(s1.name)

    for id, name, price, amount in [(1, '연필', 1000, 4),
                                    (2, '샤프', 1000, 3),
                                    (3, '지우개', 1000, 2),
                                    (4, '화이트', 1000, 1),
                                    (5, '형광펜', 1600, 4)]:
        s1.buy(Product(id, name, price), amount)

    tape = Product(6, '테이프', 1200)
    paper = Product(7, '종이', 1100)

    s1.buy(tape, 2)
    s2.buy(tape, 3)
    s2.buy(paper, 2)

    print(s1.products())
    # print(s2.products())

    # print(s2.get_product_id_by_name('종이'))
    #
    print(cur.execute("select * from stock").fetchall())  # 왜 stock의 id가 1부터 안들어가지?

    c1.buy(s1, '연필', 4)
    print(c1.purchase_list)

    print(s1.check_stock)
    print(s1.out_of_stock())




