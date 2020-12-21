"""
    一个小球从100m高度落下,每次弹回原高度一半.
   计算:
    -- 总共弹起多少次?(最小弹起高度0.01m)
    -- 全过程总共移动多少米?
"""

distance = 100
height = 100
count = 0
while height / 2 > 0.01:
    height /= 2
    distance += height * 2
    count += 1

print("总共弹起%d次,全过程总共移动%f米" % (count, distance))
