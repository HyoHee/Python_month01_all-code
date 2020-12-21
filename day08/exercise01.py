"""
    创建计算治愈比例的函数
"""


def calculate_cure_proportion(confirmed, cure):
    """
        计算治愈比例
    :param confirmed: 确诊人数
    :param cure: 治愈人数
    :return: 治愈比例
    """
    return cure / confirmed * 100


res = calculate_cure_proportion(500, 480)
print(f"治愈比例为{res}%")
