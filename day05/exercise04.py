"""
    在地区列表中删除“新疆”
    在新增列表中删除第1个元素
    在现有列表中删除前2个元素
"""

list_region = ["香港", "上海", "新疆"]
list_new = [15, 6, 0]
list_now = [393, 61, 49]

list_region.append("四川")
list_new.append(0)
list_now.append(27)

list_region.insert(0, "台湾")
list_new.insert(0, 0)
list_now.insert(0, 19)

# print(list_region)
# print(list_new)
# print(list_now)

list_region.remove("新疆")
print(list_region)
del list_new[0]
print(list_new)
del list_now[:2]
print(list_now)