"""
    定义函数，删除可迭代对象里的元素
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


def delete01():
    for i in range(len(list_employees) - 1, -1, -1):
        if list_employees[i].money > 20000:
            del list_employees[i]


def delete02():
    for i in range(len(list_employees) - 1, -1, -1):
        if list_employees[i].did == 9001:
            del list_employees[i]


def condition01(item):
    return item.money > 20000


def condition02(item):
    return item.did == 9001


def delete(func):
    for i in range(len(list_employees) - 1, -1, -1):
        if func(list_employees[i]):
            del list_employees[i]


# delete(condition01)
#
# for item in list_employees:
#     print(item.name)


# IterableHelper.delete(list_employees, lambda item: item.money > 20000)
# for item in list_employees:
#     print(item.name)

IterableHelper.delete(list_employees, lambda item: item.did==9001)
for item in list_employees:
    print(item.name)
