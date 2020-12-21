"""
    使用闭包模拟以下情景：
        在银行开户存入10000
        购买xx商品花了xx元
        购买xx商品花了xx元
"""


def save_in_bank(money):

    def buy_commodity(commodity, price):
        nonlocal money
        money -= price
        print(f"购买了{commodity},花了{price}元,还剩{money}元")

    return buy_commodity


buy = save_in_bank(10000)
buy("CD", 215)
buy("海报", 100)
buy("门票", 1680)
buy("周边", 590)
