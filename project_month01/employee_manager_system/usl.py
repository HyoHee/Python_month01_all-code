from bll import EmployeeController
from model import EmployeeModel


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
        emp.did = self.__get_number("请输入员工部门编号：")
        emp.name = input("请输入员工姓名：")
        emp.money = self.__get_number("请输入员工薪资：")
        self.__controller.add_employee(emp)
        print("添加成功")

    def __display_employee_info(self):
        for item in self.__controller.employee_list:
            print(item)

    def __remove_employee_info(self):
        eid = self.__get_number("请输入需要删除的员工编号：")
        if self.__controller.remove_employee(eid):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_employee_info(self):
        emp = EmployeeController()
        emp.eid = self.__get_number("请输入需要修改的员工编号：")
        emp.did = self.__get_number("请输入需要修改的员工部门编号：")
        emp.name = input("请输入需要修改的员工姓名：")
        emp.money = self.__get_number("请输入需要修改的员工薪资：")
        if self.__controller.update_employee_info(emp):
            print("修改成功")
        else:
            print("修改失败")

    def __get_number(self,massage):
        while True:
            try:
                number = int(input(massage))
                return number
            except:
                print("请重新输入")