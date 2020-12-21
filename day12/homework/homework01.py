"""
    完成下列功能
"""


class Wife:
    def __init__(self, name="", height=0, face_score=0):
        self.name = name
        self.height = height
        self.face_score = face_score

    def __str__(self):
        return f"{self.name}的身高是{self.height},颜值是{self.face_score}."

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.face_score > other.face_score


list_wife = [
    Wife("双儿", 170, 98),
    Wife("阿珂", 173, 100),
    Wife("苏荃", 160, 99),
    Wife("丽丽", 167, 90),
    Wife("芳芳", 168, 92),
    Wife("苏荃", 160, 99),
]

# 根据格式打印老婆对象:xx的身高是xx,颜值是xx.
print(Wife("双儿", 170, 98))

# 判断阿珂是否在列表中
print(Wife("阿珂") in list_wife)


# 计算苏荃在列表中存在的个数list_wife.count(Wife("苏荃"))
print(list_wife.count(Wife("苏荃")))

# 查找颜值最高的老婆对象max(list_wife)
print(max(list_wife))

# 根据颜值对老婆列表进行升序排列
list_wife.sort()
for item in list_wife:
    print(item)
