"""
    创建自定义range类，实现下列效果.
        class MyRange:
            pass

        for number in MyRange(5):
                print(number)# 0 1 2 3 4
"""


class MyRangeIterator:
    def __init__(self, end):
        self.__end = end
        self.__start = -1

    def __next__(self):
        self.__start += 1
        if self.__start > self.__end - 1:
            raise StopIteration
        return self.__start


class MyRange:
    def __init__(self, end_number):
        self.__end_number = end_number

    def __iter__(self):
        return MyRangeIterator(self.__end_number)


for number in MyRange(5):
    print(number)  # 0 1 2 3 4
