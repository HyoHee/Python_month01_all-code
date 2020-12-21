"""
    写出下列代码表达的命题含义
        print(666 == "666")
        print(input("你爱我吗? ") == "爱")
        print(float(input("请输入你的身高：")) > 170)
    根据命题写出代码
        输入的是正数
        输入的是月份
        输入的不是偶数
"""

print(666 == "666")  # false
print(input("你爱我吗? ") == "爱")  # 爱
print(float(input("请输入你的身高：")) > 170)  # 大于170的身高

# 输入的是正数
print(float(input("请输入一个数字：")) > 0)
# 输入的是月份
print(1 <= int(input("请输入一个月份：")) <= 12)
# 输入的不是偶数
print(int(input("请输入一个数字：")) % 2 != 0)
