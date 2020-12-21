"""
    在终端中录入5个疫情省份的确诊人数
    最后打印最大值、最小值、平均值.
    （使用内置函数实现）
"""

list_temp = []
for i in range(5):
    number = int(input(f"请输入第{i + 1}个省份的确诊人数："))
    list_temp.append(number)

print("最大值是：%d" % max(list_temp))
print("最小值是：%d" % min(list_temp))
print("平均值是：%.2f" % (sum(list_temp) / len(list_temp)))
