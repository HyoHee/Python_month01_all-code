"""
    打印香港疫情信息(xx地区新增xx人现存xx人)
    将地区列表后2个元素修改为 ["XJ","SC"]
    打印地区列表元素(一行一个)
    倒序打印新增列表元素(一行一个)
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

region = list_region[1]
new = list_new[1]
now = list_now[1]
print(f"{region}地区新增{new}人现存{now}人")
print("%s地区新增%d人现存%d人" % (region, new, now))

list_region[-2:] = ["XJ", "SC"]
print(list_region)

for item in list_region:
    print(item)

for i in range(len(list_new) - 1, -1, -1):
    print(list_new[i])
