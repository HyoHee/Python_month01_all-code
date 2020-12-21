"""
    在终端中录入五个人的身高，计算平均高度
"""
sum_value = 0
for i in range(5):
    sum_value += int(input("请输入身高："))
print("平均身高是：" + str(sum_value / 5))
