"""
    函数参数
        形式参数
            命名关键字形参
"""

# 命名关键字形参:星号后面的形参
def func01(*args, p1, p2):
    print(args)
    print(p1)
    print(p2)

# p1是位置形参,p2是命名关键字形参
def func02(p1,*,  p2=0):
    print(p1)
    print(p2)

#
func02(1,p2=2)

