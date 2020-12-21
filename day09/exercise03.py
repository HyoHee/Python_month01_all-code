"""
    创建手机类
"""


class Phone:
    def __init__(self, band=None, price=None, color=None):
        self.brand = band
        self.price = price
        self.color = color

    def call(self):
        print(self.brand + "通话")


phone01 = Phone("苹果", 6999, "白色")
phone02 = Phone("华为", 4999, "黄色")

print(phone02.brand)

phone01.call()
phone02.call()
