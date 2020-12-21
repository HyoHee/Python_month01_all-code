"""
    定义函数,在列表中找出所有数字
"""

list01 = [43, "悟空", True, 56, "八戒", 87.5, 98]


def get_number():
    for item in list01:
        if type(item) in (float, int):
            yield item


re = get_number()
for item in re:
    print(item)
