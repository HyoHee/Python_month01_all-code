"""
    以面向对象思想,描述下列情景.
        小明请保洁打扫卫生
"""


# 1
class Person:
    def __init__(self, name=""):
        self.name = name

    def engage(self, who):
        print("雇佣", who)
        clear = Cleaner()
        clear.do_clear()


class Cleaner:
    def do_clear(self):
        print("打扫卫生")


xm = Person("小明")
xm.engage("保洁")


# 2
class Person:
    def __init__(self, name=""):
        self.name = name
        self.__clear = Cleaner()

    def engage(self, who):
        print("雇佣", who)
        self.__clear.do_clear()


class Cleaner:
    def do_clear(self):
        print("打扫卫生")


xm = Person("小明")
xm.engage("保洁")


# 3
class Person:
    def __init__(self, name=""):
        self.name = name

    def engage(self, who, clearperson):
        print("雇佣", who)
        clearperson.do_clear()


class Cleaner:
    def do_clear(self):
        print("打扫卫生")


xm = Person("小明")
ay = Cleaner()
xm.engage("保洁", ay)
