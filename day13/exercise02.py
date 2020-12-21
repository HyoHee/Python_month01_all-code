"""
    说出图形管理器中,设计原则的体现

"""

class GraphicManager:# 负责统一管理所有图形
    def __init__(self):
        self.__graphic_list = []

    def add(self, graphic):
        if isinstance(graphic,Graphic):
            self.__graphic_list.append(graphic)

    def get_total_area(self):# 依赖倒置 方法中调用父类(图形类)方法
        total_area = 0
        for item in self.__graphic_list:# 依赖倒置 组合复用 调用图形类,实际执行子类方法
            # 迪米特法则 类和类之间传递数据越少越好
            # 里氏替换 调用父类方法
            total_area += item.calculate_area()# 开闭原则 扩展开放其他图形,但不改变图形管理器
        return total_area


class Graphic:# 依赖倒置 创建父类隔离子类变化
    def calculate_area(self):
        pass


class Circular(Graphic):# 单一职责 圆形类只计算圆形面积
    def __init__(self, r):
        self.r = r

    def calculate_area(self):# 里氏替换 对父类方法进行扩展重写 调用时实际执行子类方法
        return self.r ** 2 * 3.14


class Rectangle(Graphic):# 单一职责 矩形类计算矩形面积
    def __init__(self, legth, wide):
        self.legth = legth
        self.wide = wide

    def calculate_area(self):# 里氏替换 对父类方法进行扩展重写 调用时实际执行子类方法
        return self.legth * self.wide
