"""
    以面向对象思想，描述下列情景：
    情景：手雷爆炸，可能伤害敌人(头顶爆字)或者玩家(碎屏)。
    变化：还可能伤害房子、树、鸭子....
    要求：增加新事物，不影响手雷.
    画出架构设计图
"""

class Antitank:
    def boom(self, target):
        print("爆炸")
        target.damage()

class Traget:
    def damage(self):
        pass

class Emery(Traget):
    def damage(self):
        print("头顶爆字")

class Player(Traget):
    def damage(self):
        print("碎屏")

a01=Antitank()
e01=Emery()
p01=Player()
a01.boom(e01)
a01.boom(p01)