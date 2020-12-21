"""
    面向对象
        创建桌子类
        数据：品牌,材质,尺寸(长,宽,高)
   创建电脑类
        数据:型号,CPU型号,内存大小,硬盘大小
        行为：开机,关机
"""


class Table:
    def __init__(self, brand, material, size):
        self.brand = brand
        self.material = material
        self.size = size


class Computer:
    def __init__(self, model, CPU, RAM, caliche):
        self.model = model
        self.CPU = CPU
        self.RAM = RAM
        self.caliche = caliche

    def open(self):
        print(self.model + "开机")

    def close(self):
        print(self.model + "关机")
