"""
    定义函数，在员工列表中查找编号是1003的员工
    定义函数，在员工列表中查找姓名是孙悟空的员工
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


def find_eid():
    for item in list_employees:
        if item.eid ==1001:
            return item


def find_name():
    for item in list_employees:
        if item.name == "孙悟空":
            return item


def find_sigle(iterable, func):
    for item in iterable:
        if func():
            return item

def condition01(item):
    return item.eid ==1003

def condition02(item):
    return item.name =="孙悟空"

emp=IterableHelper.find_sigle(list_employees,condition01)
print(emp.__dict__)

emp02=IterableHelper.find_sigle(list_employees,condition02)
print(emp02.__dict__)