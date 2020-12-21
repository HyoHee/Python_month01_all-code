"""
    复合运算符重载减法和乘法
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x轴分量是{self.x},y轴分量是{self.y}"

    def __isub__(self, other):
        if type(other) == Vector2:
            self.x -= other.x
            self.y -= other.y
        else:
            self.x -= other
            self.y -= other
        return self

    def __mul__(self, other):
        if type(other) == Vector2:
            self.x *= other.x
            self.y *= other.y
        else:
            self.x *= other
            self.y *= other
        return self


pos01 = Vector2(3, 5)
pos01 *= Vector2(7, 3)
pos02 = Vector2(9, 9)
pos02 -= Vector2(3, 2)
print(pos01)
print(pos02)
