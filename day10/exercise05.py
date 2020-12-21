"""
    创建敌人类，并保护数据在有效范围内
          数据:姓名/ 攻击力/  血量
                     0-100   0-500
"""


class Enemy:
    def __init__(self, name="", atk=0, blood=0):
        self.name = name
        self.atk = atk
        self.blood = blood

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if 0 <= value <= 100:
            self.__atk = value
        else:
            raise Exception("攻击力有误")

    @property
    def blood(self):
        return self.__blood

    @blood.setter
    def blood(self, value):
        if 0 <= value <= 500:
            self.__blood = value
        else:
            raise Exception("血量有误")


e01 = Enemy("敌人1", 40, 180)
print(e01.blood)

e02 = Enemy("敌人2", 200, 999)
print(e02.atk)
