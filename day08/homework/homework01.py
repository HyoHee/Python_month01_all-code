"""
    定义函数,计算社保缴纳费用
"""

def calculate_insurance(money):
    """
        计算社保费用
    :param money: 税前薪资，float类型
    :return: 计算后社保缴纳费用，float类型
    """
    return money * (0.08 + 0.02 + 0.002 + 0.12) + 3

print(f"需要交纳社保：{calculate_insurance(10000)}元")
