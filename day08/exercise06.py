"""
    创建函数,根据年龄计算人生阶段
"""


def get_lift_level(age):
    """
        根据年龄判断人生阶段
    :param age: 需要判断的年龄，int类型
    :return: 判断后的结果
    """
    if age <= 6: return "童年"
    if age <= 17: return "少年"
    if age <= 40: return "青年"
    if age <= 65: return "中年"
    return "老年"

age = int(input("请输入年龄："))
print(get_lift_level(age))
