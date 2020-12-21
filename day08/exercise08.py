"""
    创建降序排列函数
"""


def subdue_ranking(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] < list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]

list01 = [5, 15, 25, 35, 1, 2]
subdue_ranking(list01)
print(list01)