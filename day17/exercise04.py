"""
    定义函数，在列表中查找奇数
    定义函数，在列表中查找能被3或5整除的数字
"""
list01 = [12, 35, 62, 57, 231, 67, 2, 6]


def find_odd():
    for item in list01:
        if item % 2 :
            yield item


def find_divide():
    for item in list01:
        if item % 3 == 0 or item % 5 == 0:
            yield item


def find_all(func):
    for item in list01:
        if func(item):
            yield item


def condition01(item):
    return item % 2


def condition02(item):
    return item % 3 == 0 or item % 5 == 0


for item in find_all(condition01):
    print(item)

for item in find_all(condition02):
    print(item)
