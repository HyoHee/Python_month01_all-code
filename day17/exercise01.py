"""
    将列表中所有奇数设置为None
    将列表中所有偶数自增1
"""

list01 = [9273, 2198, 13, 46, 7, 1234, 45, 6]
#
# for i, item in enumerate(list01):
#     if item % 2 != 0:
#         list01[i] = None

# print(list01)

list02 = [93, 456, 6, 78, 2, 1, 46, 76, 8]
for i, item in enumerate(list02):
    if item % 2 == 0:
        list02[i] += 1

print(list02)

# dict01 = {"a": 1, "b": 2, "c": 3}
#
# for i, item in enumerate(dict01):
#     print(i, item)
