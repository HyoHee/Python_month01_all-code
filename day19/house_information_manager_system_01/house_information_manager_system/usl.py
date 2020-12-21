"""
    界面处理逻辑
"""
from bll import HouseManagerController


class HouseManagerView:
    def __init__(self):
        self.__controller = HouseManagerController()

    def __display_menu(self):
        print("1) 显示所有房源信息")
        print("2) 显示总价最高的房源信息")
        print("3) 显示面积最小的房源信息")
        print("4) 根据总价升序显示房源信息")
        print("5) 根据面积降序显示房源信息")
        print("6) 查找所有户型信息")

    def __select_menu(self):
        number = input("请输入选项：")
        if number == "1":
            self.__show_all_house_info()

        elif number == "2":
            self.__get_max_total_price()

        elif number == "3":
            self.__get_min_area()

        elif number == "4":
            self.__order_by_total_price()

        elif number == "5":
            self.__order_by_area()

        elif number == "6":
            self.__find_house_type_info()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __show_all_house_info(self):
        for item in self.__controller.list_houses:
            print(item)

    def __get_max_total_price(self):
        print(self.__controller.get_max_price())

    def __get_min_area(self):
        print(self.__controller.get_min_area())

    def __order_by_total_price(self):
        list_result = self.__controller.order_by_price()
        for item in list_result:
            print(item)

    def __order_by_area(self):
        list_result = self.__controller.order_by_area()
        for item in list_result:
            print(item)

    def __find_house_type_info(self):
        dict_result = self.__controller.find_house_type()
        for k, v in dict_result.items():
                print(f"{k}　{v}个")
