"""
    面向过程练习
"""
list_commodity_infos = [
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]

# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]


def print_info(item):
    print(f"商品编号{item['cid']}, 商品名称{item['name']}, 商品单价{item['price']}.")


# 定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.

def print_commodity_info():
    for item in list_commodity_infos:
        print_info(item)


# print_commodity_info()

# 定义函数,打印商品单价小于2万的商品信息

def print_commodity_lt_price():
    for item in list_commodity_infos:
        if item["price"] < 20000:
            print_info(item)


# print_commodity_lt_price()

# 定义函数,打印所有订单中的商品信息
def print_order_info():
    for order in list_orders:
        for commodity in list_commodity_infos:
            if order["cid"] == commodity["cid"]:
                print(f"商品名称{commodity['name']},商品单价:{commodity['price']},数量{order['count']}.")
                break


# print_order_info()


# 定义函数,在商品列表中查找最贵的商品

def get_max_price_commodity():
    max_price = list_commodity_infos[0]
    for i in range(1, len(list_commodity_infos)):
        if max_price["price"] > list_commodity_infos[i]["price"]:
            max_price = list_commodity_infos[i]
    return max_price


# print(get_max_price_commodity())


# 定义函数,根据单价对商品列表升序排列

def order_by_price():
    for r in range(len(list_commodity_infos) - 1):
        for c in range(r + 1, len(list_commodity_infos)):
            if list_commodity_infos[r]["price"] > list_commodity_infos[c]["price"]:
                list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]


# order_by_price()
# print(list_commodity_infos)

# 定义函数,删除单价大于5000的商品

def delete_by_price():
    for i in range(len(list_commodity_infos) - 1, -1, -1):
        if list_commodity_infos[i]["price"] > 5000:
            del list_commodity_infos[i]

# delete_by_price()
# print(list_commodity_infos)
