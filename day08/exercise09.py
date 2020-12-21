"""
    将列表中大于某个值的元素设置为None
"""


def set_gt_number(list_target, number):
    """
        将列表中大于某个值的元素设置为None
    :param list_target: 需要更改的列表
    :param number: 大于的值，int类型
    """
    for i in range(len(list_target)):
        if list_target[i] > number:
            list_target[i] = None


list01 = [34, 545, 56, 7, 78, 8]
list02 = [34, 545, 56, 7, 78, 8]
set_gt_number(list01, 10)
set_gt_number(list02, 100)
print(list01)
print(list02)
