"""
    定义函数，根据薪资对员工列表进行升序排列
    定义函数，根据员工编号对员工列表进行升序排列
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


def order_by01():
    for r in range(len(list_employees) - 1):
        for c in range(r+1, len(list_employees)):
            if list_employees[r].money > list_employees[c].money:
                list_employees[r], list_employees[c] = list_employees[c], list_employees[r]


def order_by02():
    for r in range(len(list_employees) - 1):
        for c in range(r+1, len(list_employees)):
            if list_employees[r].eid > list_employees[c].eid:
                list_employees[r], list_employees[c] = list_employees[c], list_employees[r]

def conditon01(item):
    return item.money

def conditon02(item):
    return item.eid

def order_by(condition01):
    for r in range(len(list_employees) - 1):
        for c in range(r+1, len(list_employees)):
            if condition01(list_employees[r]) > condition01(list_employees[c]):
                list_employees[r], list_employees[c] = list_employees[c], list_employees[r]


IterableHelper.order_by(list_employees,lambda item:item.money)
# for item in list_employees:
#     print(item.name)

IterableHelper.order_by(list_employees,lambda item:item.eid)
for item in list_employees:
    print(item)
