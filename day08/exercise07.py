"""
    创建函数,根据年月计算天数.
"""


def if_leap_year(year):
    """
        判断是否为闰年
    :param year: 需要判断的年份，int类型
    :return: 是否为闰年，bool类型
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def get_days(year, month):
    """
        判断天数
    :param year: 需要判断的年份，int类型
    :param month: 需要判断的月份，int类型
    :return: 判断后的结果，int类型
    """
    if month < 1 or month > 12:
        return
    if month == 2:
        return 29 if if_leap_year(year) else 28
    if month(4, 6, 9, 11):
        return 30
    return 31


print(get_days(2019, 2))
