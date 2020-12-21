"""
    在终端中获取一个整数，作为边长，打印矩形。
"""
number = int(input("请输入边长："))
for i in range(number):
    if i == 0 or i == number - 1:
        print("*" * number)
    else:
        print("*%s*" % (" " * (number - 2)))
