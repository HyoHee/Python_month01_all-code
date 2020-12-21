"""
    画出内存图
"""

data01=10
def func01():
    data01=20

func01()

data02=[10]
def func02():
    data02[0]=20
func02()

print(data01)
print(data02)