"""
    删除香港现有人数信息
    删除新疆新增人数信息
    删除上海的新增和现有信息
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

# 删除香港现有人数信息
del dict_HK["now"]
print(dict_HK)

# 删除新疆新增人数信息
del dict_XJ["new"]
print(dict_XJ)

# 删除上海的新增和现有信息
del dict_SH["new"], dict_SH["now"]
print(dict_SH)
