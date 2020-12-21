"""
    创建函数,计算IQ等级
"""


def calculate_level(ma, ca):
    """
        计算IQ等级
    :param ma: 心理年龄，int类型
    :param ca: 实际年龄，int类型
    :return: IQ等级，str类型
    """
    iq = ma / ca * 100
    if 140 <= iq: return "天才"
    if 120 <= iq: return "超常"
    if 110 <= iq: return "聪慧"
    if 90 <= iq: return "正常"
    if 80 <= iq: return "迟钝"
    return "低能"


ma = int(input("请输入你的心里年龄："))
ca = int(input("请输入你的实际年龄："))
print(calculate_level(ma,ca))
