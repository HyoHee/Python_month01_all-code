"""
    创建狗类
        数据：品种、昵称、身长、体重
            行为：吃(体重增长1)
            实例化两个对象并调用其函数
            画出内存图
"""


class Dog:
    def __init__(self, breed="", name="", height=0, weight=0):
        self.breed = breed
        self.name = name
        self.height = height
        self.weight = weight

    def eat(self):
        print("吃")
        self.weight += 1


dog01 = Dog("金毛", "哈哈", 17, 13)
dog02 = Dog("拉布拉多", "拉拉", 29,30)
print(dog01.weight)
dog01.eat()
print(dog01.name + "体重是:" + str(dog01.weight))
dog01.eat()
print(dog01.weight)

print(dog01.__dict__)
print(dog02.__dict__)
