"""
    使用封装数据的思想
       创建员工类/部门类,修改实现下列功能.
"""


class Employees:
    def __init__(self, eid=0, did=0, name="", money=0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money


class Departments:
    def __init__(self, did=0, title=""):
        self.did = did
        self.title = title


# 员工列表
list_employees = [
    Employees(1001, 9002, "师父", 60000),
    Employees(1002, 9001, "孙悟空", 50000),
    Employees(1003, 9002, "猪八戒", 20000),
    Employees(1004, 9001, "沙僧", 30000),
    Employees(1005, 9001, "小白龙", 15000),
]

# 部门列表
list_departments = [
    Departments(9001, "教学部"),
    Departments(9002, "销售部")
]


def print_all_info(employees):
    print(f"{employees.name}的员工编号是{employees.eid}, 部门编号是{employees.did}, 月薪{employees.money}元.")


# 1.定义函数, 打印所有员工信息, 格式：xx的员工编号是xx, 部门编号是xx, 月薪xx元.
def print_all_employees():
    for employees in list_employees:
        print_all_info(employees)


# print_all_employees()

# 2.定义函数, 打印所有月薪大于2w的员工信息, 格式：xx的员工编号是xx, 部门编号是xx, 月薪xx元.
def print_all_employees_gt_2w():
    for elpoyees in list_employees:
        if elpoyees.money > 20000:
            print_all_info(elpoyees)



# print_all_employees_gt_2w()

# 3.定义函数, 打印所有员工的部门信息, 格式：xx的部门是xx, 月薪xx元.
def all_employees_department():
    for employees in list_employees:
        for departments in list_departments:
            if employees.did == departments.did:
                print(f"{employees.name}的部门是{departments.title}, 月薪{employees.money}元.")
                break

# all_employees_department()

# 4.定义函数, 查找薪资最少的员工
def get_min_money():
    min_value = list_employees[0]
    for i in range(1, len(list_employees)):
        if min_value.money > list_employees[i].money:
            min_value = list_employees[i]

    return min_value

# print(get_min_money())

# 5.定义函数, 根据薪资对员工列表升序排列
def order_by_money():
    for r in range(len(list_employees)-1):
        for c in range(r+1,len(list_employees)):
            if list_employees[r].money>list_employees[c].money:
                list_employees[r],list_employees[c]=list_employees[c],list_employees[r]

order_by_money()
# for item in list_employees:
#     print(item.name,item.money)
