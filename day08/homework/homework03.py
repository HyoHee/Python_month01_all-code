"""
    定义函数,将列表中奇数删除
"""


def delete_odd(list_target):
    for i in range(len(list_target) - 1, -1, -1):
        if list_target[i] % 2 != 0:
            del list_target[i]  # 使用remove会再次循环


list01 = [3, 7, 5, 6, 7, 8, 9, 13]
delete_odd(list01)
print(list01)
