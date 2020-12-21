"""
    根据月日,计算是这一年的第几天.
    公式：前几个月总天数 + 当月天数
        例如：5月10日
        计算：31  29  31  30 + 
"""
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))
total_days = day

day_of_month02 = 29 if year % 4 == 0 and\
                       year % 100 != 0 or year % 400 == 0 else 28
day_of_month = (31, day_of_month02, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
for item in range(month - 1):
    total_days += day_of_month[item]

print(total_days)
