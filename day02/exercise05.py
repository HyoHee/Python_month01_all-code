"""
    在终端中输入商品单价、购买的数量和支付金额。
    计算应该找回多少钱。
"""

price = float(input("请输入商品单价："))
number = int(input("请输入购买数量："))
money = float(input("请输入支付金额："))
result = money - price * number
print("应找回：" + str(result))
