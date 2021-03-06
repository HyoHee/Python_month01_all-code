"""
    定义函数，在员工列表中查找所有薪资大于20000的员工数量
    定义函数，在员工列表中查找所有部门编号是9001的员工数量
"""
from common.iterable_tools import IterableHelper


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money


list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]


# def get_count01():
#     total_count = 0
#     for item in list_employees:
#         if item.money > 20000:
#             total_count += 1
#     return total_count
#
#
# def get_count02():
#     total_count = 0
#     for item in list_employees:
#         if item.did == 9001:
#             total_count += 1
#     return total_count
#
#
# def condition01(item):
#     return item.money > 20000
#
# def coudition02(item):
#     return item.did == 9001
#
# def get_count(func):
#     total_count = 0
#     for item in list_employees:
#         if func(item):
#             total_count += 1
#     return total_count


print(IterableHelper.get_count(list_employees, lambda item: item.money > 20000))
print(IterableHelper.get_count(list_employees, lambda item: item.did == 9001))


