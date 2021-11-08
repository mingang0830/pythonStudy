import sqlite3

conn = sqlite3.connect('store_sys.db')
cur = conn.cursor()

# SOLID
# S: 단일 책임의 원칙

# product_db.py
def make_product_map(data):
    return {
        "id": data[0],
        "name": data[1],
        "price": data[2],
    }

def select_product_by_id_from_db(id):
    return cur.execute("select id, name, price from product where id = (?)", (id,)).fetchone()

def insert_product_to_db(name, price):
    return cur.execute("insert into product (name, price) values(?,?)", (name, price))

# new_product_db.py
def select_new_product_by_id_from_db(id):
    pass

# product_model.py
def get_product_by_id(id):
    data = select_new_product_by_id_from_db(id)
    return make_product_map(data)

def create_product(name, price):
    return make_product_map(insert_product_to_db(name, price))

# product_obj.py
# CQRS 명령과 쿼리의 분리
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"('{self.name}', {self.price})"

def get_product_obj_by_id(id):
    data = get_product_by_id(id)
    return Product(id=data["id"], name=data["name"], price=data["price"])

def program1():
    get_product_obj_by_id(1)

def program2():
    Product(id=2, name="test", price=12000)


class Store:
    def __init__(self, id, name):
        cur.execute("insert into store values({}, '{}')".format(id, name))
        self.id = id
        self.name = name
        self.check_stock = {}
        self.products = {}

    def buy(self, product, amount):
        cur.execute("insert into stock (store_id, product_id) values(?,?)", (self.id, product.id))
        self.check_stock[product] = amount
        self.products[product.id] = product

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
        product = store.products[product_id]
        new_amount = store.check_stock[product] - amount

        if new_amount >= 0:
            store.check_stock[product] = new_amount
            self.purchase_list.append({'store': store, 'product': product, 'amount': amount})
            print(f'{product} - {amount}개 구매완료!')
        else:
            raise Exception('상품의 재고가 부족합니다.')


if __name__ == "__main__":
    cur.execute("insert into product (name, price) values(?,?)", ("가위", 1000))
    # prepared statement
    p1 = Product(name="풀", price=1000)

    # print(p1)
    # s1 = Store(1, '문방구')
    # s2 = Store(2, '문방구2')
    # c1 = Customer()
    # print(s1.id)
    # print(s1.name)

    # for id, name, price, amount in [(1, '연필', 1000, 4),
    #                                 (2, '샤프', 1000, 3),
    #                                 (3, '지우개', 1000, 2),
    #                                 (4, '화이트', 1000, 1),
    #                                 (5, '형광펜', 1600, 4)]:
    #     s1.buy(Product(id, name, price), amount)
    #
    # tape = Product(6, '테이프', 1200)
    # paper = Product(7, '종이', 1100)
    #
    # s1.buy(tape, 2)
    # s2.buy(tape, 3)
    # s2.buy(paper, 2)
    #
    # print(s1.products)
    # print(s2.products())

    # print(s2.get_product_id_by_name('종이'))
    #
    # print(cur.execute("select * from stock").fetchall())  # 왜 stock의 id가 1부터 안들어가지?

    # c1.buy(s1, '연필', 4)
    # print(c1.purchase_list)
    #
    # print(s1.check_stock)
    # print(s1.out_of_stock())




