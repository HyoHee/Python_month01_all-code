"""
    打印信息
"""

dict_employees = {
    1001: {"did": 9002, "name": "师父", "money": 60000},
    1002: {"did": 9001, "name": "孙悟空", "money": 50000},
    1003: {"did": 9002, "name": "猪八戒", "money": 20000},
    1004: {"did": 9001, "name": "沙僧", "money": 30000},
    1005: {"did": 9001, "name": "小白龙", "money": 15000},
}

list_departments = [
    {"did": 9001, "title": "教学部"},
    {"did": 9002, "title": "销售部"},
    {"did": 9003, "title": "品保部"},
]

# 打印所有员工信息

for k, v in dict_employees.items():
    print("%s的员工编号是%d,部门编号是%d,月薪%d元." %
          (v["name"], k, v["did"], v["money"]))
# for value in dict_employees.values():
#     for item in list_departments:
#         if value["did"] ==item["did"]:
#             print(item["title"])

# 打印所有月薪大于2w的员工信息

for k, v in dict_employees.items():
    if v["money"] > 20000:
        print("%s的员工编号是%d,部门编号是%s,月薪%s元." %
              (v["name"], k, v["did"], v["money"]))

# 在部门列表中查找编号最小的部门

min_department = list_departments[0]
for i in range(1, len(list_departments)):
    if min_department["did"] > dict_employees[i]["did"]:
        min_department = dict_employees[i]
print(min_department)

# 根据部门编号对部门列表降序排列

for r in range(len(list_departments) - 1):
    for c in range(r + 1, len(list_departments)):
        if list_departments[r]["did"] < list_departments[c]["did"]:
            list_departments[r], list_departments[c] = list_departments[c], list_departments[r]
print(list_departments)
