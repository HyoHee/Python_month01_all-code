"""
    在终端中录入疫情地区名称，如果输入空字符串，则停止。
    最后倒序打印所有地区名称(一行一个)
    要求：录入的名称已经存在不要再次添加.
"""

list_region = []
while True:
    region = input("请输入疫情地区名称：")
    if region == "":
        break
    if region in list_region:
        print("请勿重复添加")
        continue
    list_region.append(region)
for item in list_region[::-1]:
    print(item)

for i in range(len(list_region) - 1, -1, -1):
    print(item)
