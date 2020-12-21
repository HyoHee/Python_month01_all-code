"""
    定义函数,根据生日(年月日),计算活了多天.
        输入：2010   1   1
        输出：从2010年1月1日到现在总共活了3910天
"""

import time


def get_total_days(year, month, day):
    str_time = "%d/%d/%d" % (year, month, day)
    time_tuple = time.strptime(str_time, "%Y/%m/%d")
    time_input = time.mktime(time_tuple)
    time_diffence = time.time() - time_input
    days = time_diffence // 3600 // 24
    return "总共活了%d天" % days


print(get_total_days(1994, 7, 14))
