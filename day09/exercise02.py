"""
    定义数值累乘函数
"""

def number_multiplicate(*args):
    res=1
    for item in args:
        res*=item
    return res

list01=[2,4,5,2,7,9]

print(number_multiplicate(*list01))