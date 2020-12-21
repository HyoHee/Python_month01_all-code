"""
    创建字典,使用迭代思想,打印每个键值对.
"""

dict01 = {"a": 1, "b": 2, "c": 3, "d": 4}

iterator = dict01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key, dict01[key])
    except StopIteration:
        break
