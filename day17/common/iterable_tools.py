"""
    可迭代对象助手
"""

class IterableHelper:

    @staticmethod
    def find_sigle(iterable, func):
        """
            在可迭代对象中查找满足条件的单个元素
        :param iterable: 可迭代对象
        :param func: 查找条件函数
        :return: 查找后的元素
        """
        for item in iterable:
            if func(item):
                return item
    @staticmethod
    def find_all(iterable,func):
        """
            在可迭代对象中查找满足条件的多个元素
        :param iterable: 可迭代对象
        :param func: 查找条件函数
        :return: 生成器
        """
        for item in iterable:
            if func(item):
                yield item

    @staticmethod
    def select(iterable,func):
        """
            根据条件查找
        :param iterable:
        :param func:
        :return:
        """
        for item in iterable:
            yield func(item)

    @staticmethod
    def get_count(iterable, func):
        """
            在可迭代对象中根据条件查找元素
        :param iterable: 可迭代对象
        :param func: 查找条件函数
        :return: 查找后的总数
        """
        total_count = 0
        for item in iterable:
            if func(item):
                total_count += 1
        return total_count

    @staticmethod
    def get_max(iterable, func):
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if func(max_value) < func(iterable[i]):
                max_value = iterable[i]
        return max_value

    @staticmethod
    def get_min(iterable, func):
        min_value = iterable[0]
        for i in range(1, len(iterable)):
            if func(min_value) > func(iterable[i]):
                min_value = iterable[i]
        return min_value

    @staticmethod
    def order_by(iterable, func):
        for r in range(len(iterable) - 1):
            for c in range(r + 1, len(iterable)):
                if func(iterable[r]) > func(iterable[c]):
                    iterable[r], iterable[c] = iterable[c], iterable[r]

    @staticmethod
    def delete(iterable, func):
        for i in range(len(iterable) - 1, -1, -1):
            if func(iterable[i]):
                del iterable[i]
