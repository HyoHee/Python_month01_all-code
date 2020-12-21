"""
    实现自定义类型的减法与乘法运算
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x轴分量是{self.x},y轴分量是{self.y}"

    def __sub__(self, other):
        if type(other) == Vector2:
            x = self.x - other.x
            y = self.y - other.y
        else:
            x = self.x + other
            y = self.y + other
        return Vector2(x, y)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Vector2(x, y)


pos01 = Vector2(6, 5)
pos02 = Vector2(1, 3)
pos03 = pos01 - pos02
pos04 = pos01 * pos02
print(pos03)
print(pos04)
