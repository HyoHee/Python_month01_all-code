"""
    业务逻辑层
"""
from common.iterable_tools import IterableHelper
from dal import HouseDao


class HouseManagerController:
    def __init__(self):
        self.__list_houses = HouseDao.load()

    @property
    def list_houses(self):
        return self.__list_houses

    def get_max_price(self):
        return IterableHelper.get_max(self.__list_houses, lambda item: item.total_price)

    def get_min_area(self):
        return IterableHelper.get_min(self.__list_houses, lambda item: item.area)

    def order_by_price(self):
        list_temp = self.__list_houses[:]
        IterableHelper.order_by(list_temp, lambda item: item.total_price)
        return list_temp

    def order_by_area(self):
        return sorted(self.__list_houses, key=lambda item: item.area, reverse=True)

    def find_house_type(self):
        dict_temp = {}
        for item in self.__list_houses:
            if item.house_type in dict_temp:
                dict_temp[item.house_type] += 1
            else:   
                dict_temp[item.house_type] = 1
        return dict_temp
