"""
    对数字列表进行降序排列（小 --> 大）
"""

list01 = [55, 65, 67, 76, 8, 6, 9, 64]
for r in range(len(list01) - 1):
    for c in range(r + 1, len(list01)):
        if list01[r] < list01[c]:
            list01[r], list01[c] = list01[c], list01[r]
print(list01)
