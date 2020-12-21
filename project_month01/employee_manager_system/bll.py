from model import EmployeeModel


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