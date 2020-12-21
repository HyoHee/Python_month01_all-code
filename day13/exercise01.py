"""
    创建图形管理器
	1. 记录多种图形（圆形、矩形....）
	2. 提供计算总面积的方法.
    满足：
        开闭原则
    测试：
        创建图形管理器，存储多个图形对象。
        通过图形管理器，调用计算总面积方法.

    设计:
        封装(分):创建图形管理器类/圆形类/矩形类
        继承(隔):创建图形类,隔离图形管理器类与具体图形类
        继承(做):具体图形类重写图形类的计算方法
"""


class GraphicManager:
    def __init__(self):
        self.__graphic_list = []

    def add(self, graphic):
        if isinstance(graphic,Graphic):
            self.__graphic_list.append(graphic)

    def get_total_area(self):
        total_area = 0
        for item in self.__graphic_list:
            total_area += item.calculate_area()
        return total_area


class Graphic:
    def calculate_area(self):
        pass


class Circular(Graphic):
    def __init__(self, r):
        self.r = r

    def calculate_area(self):
        return self.r ** 2 * 3.14


class Rectangle(Graphic):
    def __init__(self, legth, wide):
        self.legth = legth
        self.wide = wide

    def calculate_area(self):
        return self.legth * self.wide


manager = GraphicManager()
manager.add(Circular(8))
manager.add(Rectangle(2,3))
total_area = manager.get_total_area()
print(total_area)
