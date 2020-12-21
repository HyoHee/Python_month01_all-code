"""
    在数字列表中查找最大的数字(不许用内置函数)
    算法：
        [170  ,  160  ,  180  ,  165]
"""

list01 = [170, 160, 180, 165]
max_value = list01[0]

for i in range(1, len(list01)):
    if max_value < list01[i]:
        max_value = list01[i]

print(max_value)
