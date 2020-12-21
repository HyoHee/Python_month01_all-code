"""
    湖北确诊67802人,治愈63326人,治愈率0.99
    70秒是01分零10秒
"""
location = "湖北"
diagnose = 67802
cure = 63326
proportion = 0.99
# print("%s确诊%d人,治愈%d人,治愈率%.2f" % (location, diagnose, cure, proportion))
print(f"{location}确诊{diagnose}人,治愈{cure}人,治愈率{proportion}")

total_second = 70
minute = total_second // 60
second = total_second % 60
print("%d秒是%.2d分零%.2d秒" % (total_second, minute, second))
