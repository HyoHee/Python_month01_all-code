"""
    面向过程 2048游戏核心算法
"""
list_merge = [2, 0, 0, 2]


# 定义函数,零元素移动到末尾

def zero_to_end(list_target):
    """
    将零元素移动到末尾
    """
    for i in range(len(list_target) - 1, -1, -1):
        if list_target[i] == 0:
            del list_target[i]
            list_target.append(0)


zero_to_end(list_merge)
print(list_merge)

# 定义函数,相邻相同数字合并
def sum_same_element(list_target):
    """
        合并相邻相同元素
    """
    zero_to_end(list_target)
    for i in range(len(list_target)-1):#len(list_target)
        if list_target[i] == list_target[i + 1]:
            list_target[i] += list_target[i + 1]
            del list_target[i + 1]
            list_target.append(0)

sum_same_element(list_merge)
print(list_merge)

