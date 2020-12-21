"""
    定义函数,根据小时、分钟、秒,计算总秒数
"""


def total_second(hour=0, minute=0, second=0):
    return hour * 3600 + minute * 60 + second


# 调用：提供小时、分钟、秒
print(total_second(1, 5, 30))

# 调用：提供分钟、秒
print(total_second(minute=7, second=9))

# 调用：提供小时、秒
# 位置实参+关键词实参
print(total_second(9, second=50))

# 调用：提供分钟
print(total_second(minute=58))
