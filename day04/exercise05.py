"""
    在终端中录入五个人的身高，如果录入空字符串，
    则停止录入，再计算平均高度
"""
total_height = 0
count = 0
while True:
    height = input("请输入身高：")
    if height == "":
        break
    count += 1
    total_height += int(height)
print("平均身高是：" + str(total_height / count))
