"""
    以面向对象思想,描述下列情景.
        玩家攻击敌人,敌人受伤(根据玩家攻击力，减少敌人的血量).
"""


class Player:
    def __init__(self, atk=0):
        self.atk = atk

    def do_atk(self, enemy):
        print("攻击")
        enemy.injure(self.atk)


class Enemry:
    def __init__(self, hp=0):
        self.hp = hp

    def injure(self, value):
        self.hp -= value
        print(self.hp)


player = Player(10)
enemry = Enemry(100)
player.do_atk(enemry)


