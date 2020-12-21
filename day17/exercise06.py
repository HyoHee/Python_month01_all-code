"""
    使用lambda表达式改exercise05
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


emp = IterableHelper.find_sigle(list_employees, lambda item: item.name == "孙悟空")
print(emp)

emp02 = IterableHelper.find_sigle(list_employees, lambda item: item.eid == 1003)
print(emp02.__dict__)
