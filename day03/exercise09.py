"""
    在终端中输入一个年份，如果是闰年为变量day赋值29,否则赋值28。
      闰年条件：年份能被4整除但是不能被100整除
                年份能被400整除
    效果：
        请输入年份:2020
    2020年的2月有29天
"""

month = int(input("请输入一个年份："))
if month % 400 == 0 or month % 4 == 0 and month % 100:
    day = 29
else:
    day = 28
print(str(month) + "年的2月有" + str(day) + "天")
