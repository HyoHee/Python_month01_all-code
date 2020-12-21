"""
    在终端中录入4个同学年龄,打印最小的年龄。
"""

age01 = int(input("请输入年龄："))
age02 = int(input("请输入年龄："))
age03 = int(input("请输入年龄："))
age04 = int(input("请输入年龄："))

min_age = age01
if min_age > age02:
    min_age = age02
if min_age > age03:
    min_age = age03
if min_age > age04:
    min_age = age04
print(min_age)
