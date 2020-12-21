"""
    创建父类：车(品牌，速度)
    创建子类：电动车(电池容量,充电功率)
    创建子类对象并画出内存图。
"""


class Car:
    def __init__(self, brand="", speed=0):
        self.breed = brand
        self.speed = speed


class ElectricityCar(Car):
    def __init__(self, brand="", speed=0, battery_capacity=0, charge_power=0):
        super().__init__(brand, speed)
        self.battery_capacity = battery_capacity
        self.charge_power = charge_power


ec01 = ElectricityCar("小电动", 200, 500, 120)
print(ec01.breed)