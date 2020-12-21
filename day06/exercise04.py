"""
    在终端中打印香港字典的所有键(一行一个)
    在终端中打印上海字典的所有值(一行一个)
    在终端中打印新疆字典的所有键和值(一行一个)
    在上海字典中查找值是61对应的键名称
"""

dict_HK = {
    "region": "香港",
    "new": 15,
    "now": 393,
    "count": 4801,
    "cure": 4320,
    "death": 88
}
dict_SH = {
    "region": "上海",
    "new": 6,
    "now": 61,
    "count": 903,
    "cure": 835,
    "death": 7
}
dict_XJ = {
    "region": "新疆",
    "new": 0,
    "now": 49,
    "count": 902,
    "cure": 850,
    "death": 3
}

# 在终端中打印香港字典的所有键(一行一个)
for key in dict_HK:
    print(key)

# 在终端中打印上海字典的所有值(一行一个)
for value in dict_SH.values():
    print(value)

# 在终端中打印新疆字典的所有键和值(一行一个)
for item in dict_XJ.items():
    print(item)

# 在上海字典中查找值是61对应的键名称
for k, v in dict_SH.items():
    if v == 61:
        print(k)
        break
