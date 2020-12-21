"""
    以面向对象思想,描述下列情景.
        玩家攻击敌人,敌人受伤(头顶爆字).
"""


class User:
    def atk(self, enemy):
        print("攻击")
        enemy.injure()


class Enemry:
    def injure(self):
        print("受伤")
        print("头顶爆字")

u01=User()
e01=Enemry()
u01.atk(e01)
