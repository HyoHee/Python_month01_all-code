"""
    在终端中循环录入5个成绩,
    最后打印平均成绩(总成绩除以人数)
        效果：
        请输入成绩：98
        请输入成绩：83
        请输入成绩：90
        请输入成绩：99
        请输入成绩：78
        平均分：89.6
"""
count = 0
total_score = 0
while count < 5:
    score = float(input("请输入成绩："))
    total_score += score
    count += 1
average = total_score / count
print(average)
