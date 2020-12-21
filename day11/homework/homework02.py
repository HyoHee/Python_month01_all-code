"""
    小明一次请多个保洁打扫卫生
        效果:调用一次小明通知方法,可以有多个保洁在打扫卫生.
"""


class Person:
    def __init__(self, name=""):
        self.name = name

    # def notify(self, target):
    #     print("通知")
    #     for item in target:
    #         item.serve()

    def notify(self, *args):
        print("通知")
        for item in args:
            item.serve()


class Servers:
    def __init__(self, name=""):
        self.name = name

    def serve(self):
        print(self.name, "打扫")


xm = Person("小明")
list01 = [Servers("张阿姨"),Servers("李阿姨")]

xm.notify(list01)
