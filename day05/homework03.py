"""
    计算列表中字符串⻓度⼤于2，并且第⼀个和最后⼀个字符相同的字符串个数
    字符串列表：words =["qtx","看一看","想啊想","练练"]
    结果:2
"""

count = 0
words = ["qtx", "看一看", "想啊想", "练练"]
for item in words:
    if len(item) > 2 and item[0] == item[-1]:
        count += 1
print(f"结果：{count}")
