"""
    遍历图形控制器
"""


class GraphicIterator:
    def __init__(self, data):
        self.__data = data
        self.__index = -1

    def __next__(self):
        self.__index += 1
        if self.__index > len(self.__data)-1:
            raise StopIteration
        return self.__data[self.__index]


class GraphicController:
    def __init__(self):
        self.__graphic_list = []

    def add_graphic(self, graphic):
        self.__graphic_list.append(graphic)

    def __iter__(self):
        return GraphicIterator(self.__graphic_list)


controller = GraphicController()
controller.add_graphic("圆形")
controller.add_graphic("矩形")
controller.add_graphic("三角形")



for item in controller:
    print(item)
