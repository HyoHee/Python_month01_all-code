"""
    商品信息管理系统
"""


class CommodityModel:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __str__(self):
        return f"商品编号：{self.cid},商品名称：{self.name},商品价格：{self.price}"

    def __eq__(self, other):
        return self.cid == other.cid


class CommodityView:
    def __init__(self):
        self.__controller = CommodityController()

    def __display_menu(self):
        print("1) 添加商品")
        print("2) 显示商品")
        print("3) 删除商品")
        print("4) 修改商品")

    def __select_menu(self):
        number = input("请输入选项:")
        if number == "1":
            self.__input_commodity_info()
        elif number == "2":
            self.__display_commodity_info()
        elif number == "3":
            self.__delete_commodity()
        elif number == "4":
            self.__modify_commodity()

    def __input_commodity_info(self):
        commodity = CommodityModel()
        commodity.name = input("请输入商品名称:")
        commodity.price = int(input("请输入商品价格:"))
        self.__controller.add_commodity_info(commodity)
        print("添加成功")

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_commodity_info(self):
        for item in self.__controller.commodity_list:
            print(item)

    def __delete_commodity(self):
        cid = int(input("请输入需要删除的商品编号："))
        if self.__controller.remove_commodity(cid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_commodity(self):
        commodity = CommodityModel()
        commodity.cid = int(input("请输入需要修改的商品编号："))
        commodity.name = input("请输入需要修改的商品名称：")
        commodity.price = int(input("请输入需要修改的商品价格："))
        if self.__controller.update_commodity_info(commodity):
            print("修改成功")
        else:
            print("修改失败")


class CommodityController:
    def __init__(self):
        self.__commodity_list = []
        self.start_id = 1001

    @property
    def commodity_list(self):
        return self.__commodity_list

    def add_commodity_info(self, commodity):
        """
            添加商品
        :param commodity: 需要添加的商品
        """
        commodity.cid = self.start_id
        self.start_id += 1
        self.__commodity_list.append(commodity)

    def remove_commodity(self, cid):
        """
            删除商品
        :param cid: 需要移除的商品编号
        :return: 是否删除成功
        """
        commodity = CommodityModel(cid)
        if commodity in self.__commodity_list:
            self.__commodity_list.remove(commodity)
            # for item in self.__commodity_list:
            #     if item.cid == cid:
            #         self.__commodity_list.remove(item)
            return True
        return False

    def update_commodity_info(self, new_commodity):
        """
            修改商品信息
        :param new_commodity: 新商品
        :return: 是否修改成功
        """
        for item in self.__commodity_list:
            if item.cid == new_commodity.cid:
                item.__dict__ = new_commodity.__dict__
                return True
        return False


view = CommodityView()
view.main()
