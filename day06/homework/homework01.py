"""
    将列表中的数字累减
    list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
"""

list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
count = list02[0]

for i in range(1,len(list02)):
    count -= list02[i]

print(count)
