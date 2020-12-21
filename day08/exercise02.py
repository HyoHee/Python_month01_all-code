"""
    定义函数,根据总两数,计算几斤零几两
"""


def calculate_jin_liang(total_liang):
    """
        根据总两数，计算几斤零几两
    :param total_liang:总两数
    :return:计算后的斤数和两数，元组类型
    """
    jin = total_liang // 16
    liang = total_liang % 16
    return jin, liang  # 使用元组


jin, liang = calculate_jin_liang(100)
print(f"{jin}斤零{liang}两")
