"""
    定义函数，在员工列表中查找员工编号最小的员工
    定义函数，在员工列表中查找薪资最少的员工
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


def get_min01():
    min_value = list_employees[0]
    for i in range(1, len(list_employees)):
        if min_value.eid > list_employees[i].eid:
            min_value = list_employees[i]
    return min_value


def get_min02():
    min_value = list_employees[0]
    for i in range(1, len(list_employees)):
        if min_value.money > list_employees[i].money:
            min_value = list_employees[i]
    return min_value


def condition01(item):
    return item.money


def get_min(condition01):
    min_value = list_employees[0]
    for i in range(1, len(list_employees)):
        if condition01(min_value) > condition01(list_employees[i]):
            min_value = list_employees[i]
    return min_value




print(IterableHelper.get_min(list_employees, lambda item: item.eid).name)
print(IterableHelper.get_min(list_employees, lambda item: item.money).name)
