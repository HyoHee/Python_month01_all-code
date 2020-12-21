"""
    定义函数,在列表中找出所有偶数
"""

list01 = [43, 43, 54, 56, 76, 87, 98]


def get_even():
    for item in list01:
        if item % 2 == 0:
            yield item


re = get_even()
for item in re:
    print(item)
