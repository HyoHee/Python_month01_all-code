"""
    将面向过程改为面向对象
"""


class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]


class Order:
    def __init__(self, cid=0, count=0):
        self.cid = cid
        self.count = count


# 订单列表
list_orders = [
    Order(1001, 1),
    Order(1002, 3),
    Order(1005, 2),
]


def print_info(commodity):
    print(f"商品编号{commodity.cid}, 商品名称{commodity.name}, 商品单价{commodity.price}")


# 定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.

def print_commodity_info():
    for commodity in list_commodity_infos:
        print_info(commodity)


print_commodity_info()


# 定义函数,打印商品单价小于2万的商品信息

def print_commodity_lt_price():
    for commodity in list_commodity_infos:
        if commodity.price < 20000:
            print_info(commodity)


print_commodity_lt_price()


# 定义函数,打印所有订单中的商品信息
def print_order_info():
    for order in list_orders:
        for commodity in list_commodity_infos:
            if order.cid == commodity.cid:
                print(f"商品名称{commodity.name},商品单价:{commodity.price},数量{order.count}.")
                break


print_order_info()


# 定义函数,在商品列表中查找最贵的商品

def get_max_price_commodity():
    max_price = list_commodity_infos[0]
    for i in range(1, len(list_commodity_infos)):
        if max_price.price < list_commodity_infos[i].price:
            max_price = list_commodity_infos[i]
    return max_price


print(get_max_price_commodity().name)


# 定义函数,根据单价对商品列表升序排列

def order_by_price():
    for r in range(len(list_commodity_infos) - 1):
        for c in range(r + 1, len(list_commodity_infos)):
            if list_commodity_infos[r].price > list_commodity_infos[c].price:
                list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]


order_by_price()
print()


# 定义函数,删除单价大于5000的商品

def delete_by_price():
    for i in range(len(list_commodity_infos) - 1, -1, -1):
        if list_commodity_infos[i].price > 5000:
            del list_commodity_infos[i]


delete_by_price()
print(list_commodity_infos)
