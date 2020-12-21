"""
    读写属性:
    创建技能类，并保护数据在有效范围内
        数据：技能名称,冷却时间,  攻击力度,  消耗法力
                    0 -- 120  0 -- 200  100 -- 100

"""


class Skill:
    def __init__(self, name="", atk=0, cd=0, sp=0):
        self.name = name
        self.cd = cd
        self.atk = atk
        self.sp = sp

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 <= value <= 200:
            self.__atk = value
        else:
            raise Exception("攻击力超出范围")

    @property
    def cd(self):
        return self.__cd

    @cd.setter
    def cd(self, value):
        if value > 120:
            value = 120
        elif value < 0:
            value = 0
        self.__cd = value

    @property
    def sp(self):
        return self.__sp

    @sp.setter
    def sp(self, value):
        if 0<=value <= 100:
            self.__sp = value
        else:
            raise Exception()
