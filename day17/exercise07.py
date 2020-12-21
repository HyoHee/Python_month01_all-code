"""

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

#
# def select01():
#     for item in list_employees:
#         yield item.name
#
#
# def select02():
#     for item in list_employees:
#         yield item.eid, item.money
#
# def condition(item):
#     return item.eid, item.money
#
# #
# # for item in select02():
# #     print(item)
#
#
# def select(func):
#     for item in list_employees:
#         yield func(item)
#
# for item in select(condition):
#     print(item)


for item in IterableHelper.select(list_employees,lambda item:item.name):
    print(item)

