"""
    创建函数,计算梯形面积
"""


def calculate_echelon_area(top_base, bottom_base, height):
    """
        计算梯形面积
    :param top_base: 上底长度，float类型
    :param bottom_base:下底长度，float类型
    :param height:高长度，float类型
    :return: 计算后的结果，float类型
    """
    return (top_base + bottom_base) * height / 2


top_base = float(input("请输入上底："))
bottom_base = float(input("请输入下底："))
height = float(input("请输入高："))
print(calculate_echelon_area(top_base, bottom_base, height))
