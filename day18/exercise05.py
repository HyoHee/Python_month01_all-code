"""
    为sum_data,增加打印函数执行时间的功能.
"""

# 函数执行时间公式： 执行后时间 - 执行前时间
import time


def enforce_time(func):
    def wrapper(*args, **kwargs):
        before_time = time.time()
        re = func(*args, **kwargs)
        after_time = time.time()
        print("执行时间是：",after_time - before_time)
        return re

    return wrapper


@enforce_time
def sum_data(n):
    sum_value = 0
    for number in range(n):
        sum_value += number
    return sum_value


print(sum_data(10))
print(sum_data(1000000))
