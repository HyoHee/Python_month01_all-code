"""
    员工信息管理系统
"""


class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

    def __str__(self):
        return f"{self.name}的员工编号是{self.eid},部门编号是{self.did},月薪是{self.money}."

    def __eq__(self, other):
        return self.eid == other.eid


class EmpoyeeViwe:
    def __init__(self):
        self.__controller = EmployeeController()

    def __display_menu(self):
        print("1) 添加员工信息")
        print("2) 显示员工信息")
        print("3) 删除员工信息")
        print("4) 修改员工信息")

    def __select_menu(self):
        number = input("请输入选项：")
        if number == "1":
            self.__input_employee_info()
        elif number == "2":
            self.__display_employee_info()
        elif number == "3":
            self.__remove_employee_info()
        elif number == "4":
            self.__modify_employee_info()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_employee_info(self):
        emp = EmployeeModel()
        emp.did = int(input("请输入员工部门编号："))
        emp.name = input("请输入员工姓名：")
        emp.money = input("请输入员工薪资：")
        self.__controller.add_employee(emp)
        print("添加成功")

    def __display_employee_info(self):
        for item in self.__controller.employee_list:
            print(item)

    def __remove_employee_info(self):
        eid = int(input("请输入需要删除的员工编号："))
        if self.__controller.remove_employee(eid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_employee_info(self):
        emp = EmployeeController()
        emp.eid = int(input("请输入需要修改的员工编号："))
        emp.did = int(input("请输入需要修改的员工部门编号："))
        emp.name = input("请输入需要修改的员工姓名：")
        emp.money = input("请输入需要修改的员工薪资：")
        if self.__controller.update_employee_info(emp):
            print("修改成功")
        else:
            print("修改失败")


class EmployeeController:
    def __init__(self):
        self.__employee_list = []
        self.__eid = 1000

    @property
    def employee_list(self):
        return self.__employee_list

    def add_employee(self, emp):
        self.__eid += 1
        emp.eid = self.__eid
        self.__employee_list.append(emp)

    def remove_employee(self, target_eid):
        emp = EmployeeModel(target_eid)
        if emp in self.__employee_list:
            self.__employee_list.remove(emp)
            return True
        return False

    def update_employee_info(self, new_emp):
        for item in self.__employee_list:
            if item.eid == new_emp.eid:
                item.__dict__ = new_emp.__dict__
                return True
        return False


view = EmpoyeeViwe()
view.main()
