"""
    将列表中的数字累乘
   list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
   结果：806400
"""

list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
count = 1
for item in list02:
    count *= item
print(f"结果是：{count}")

