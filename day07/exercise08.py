"""
    查找内容
"""

dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}
# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]

# 打印所有订单中的信息
for item in list_orders:
    print("商品编号%s, 购买数量%d." % (item["cid"], item["count"]))

# 打印所有订单中的商品信息


for item in list_orders:
    print("商品名称%s,商品单价:%d,数量%d" % (
        dict_commodity_infos[item["cid"]]["name"],
        dict_commodity_infos[item["cid"]]["price"],
        item["count"]))

# 查找数量最多的订单(使用自定义算法,不使用内置函数)

max_order = list_orders[0]
for i in range(1, len(list_orders)):
    if max_order["count"] < list_orders[i]["count"]:
        max_order = list_orders[i]
print(max_order)

# 根据购买数量对订单列表降序(大->小)排列

for r in range(len(list_orders) - 1):
    for c in range(r + 1, len(list_orders)):
        if list_orders[r]["count"] < list_orders[c]["count"]:
            list_orders[r], list_orders[c] = list_orders[c], list_orders[r]
print(list_orders)
