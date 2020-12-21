"""
    2048核心算法
"""
list_merge = [2, 0, 0, 2]


def zero_to_end():
    """
    将零元素移动到末尾
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


zero_to_end()
print(list_merge)


# 定义函数,相邻相同数字合并
def merge():
    """
        合并相邻相同元素
    """
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


map = [
    [2, 2, 8, 16],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [0, 4, 0, 4],
]


# 定义函数,实现向左移动(操作map)
# 思想:取出每行交给list_merge,再调用merge函数处理数据

def move_lift():
    global list_merge
    for item in map:
        list_merge = item
        merge()


move_lift()
print(map)


# 定义函数,实现向右移动(操作map)
# 思想:取出每行反向切片交给list_merge,
# 再调用merge函数处理数据(操作新列表)
# 最后还给map

def move_right():
    global list_merge
    for item in map:
        list_merge = item[::-1]
        merge()
        item[::-1] = list_merge

move_right()
print(map)
