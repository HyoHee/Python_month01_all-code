"""
    函数参数
        实参参数
            序列实参：拆
        形式参数
            星号元组实参：合
"""


def func01(p1, p2, p3):
    print(p1)
    print(p2)
    print(p3)


list01 = [1, 2, 3]
tuple01 = (4, 5, 6)
dict01 = {1: "a", 2: "b", 3: "c"}
str01 = "星星星"
# 序列实参：将一个序列 拆分为 多个实参,按顺序传参
# 实用性：在其他环境中构建好实参
# func01(*list01)
# func01(*tuple01)
# func01(*str01)
# func01(*dict01)

# 星号元组形参：将多个位置实参 合并为一个元组
# 适用性：需要位置实参无限
# 只支持位置形参
def func02(*args):
    print(args)

func02(1)
func02(1,2,3)
func02(*list01)
func02(*str01)
