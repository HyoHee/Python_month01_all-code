"""
    将两个列表，合并为一个字典
	姓名列表["张无忌","赵敏","周芷若"]
	房间列表[101,102,103]
    {101: '张无忌', 102: '赵敏', 103: '周芷若'}

    颠倒练习1字典键值
    {'张无忌': 101, '赵敏': 102, '周芷若': 103}
"""
list_name = ["张无忌", "赵敏", "周芷若"]
list_room = [101, 102, 103]

dict_result = {}

for i in range(3):
    dict_result[list_room[i]] = list_name[i]
print(dict_result)

dict_result_new = {v: k for k, v in dict_result.items()}
print(dict_result_new)
