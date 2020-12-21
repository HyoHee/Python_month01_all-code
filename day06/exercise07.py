"""
     "经理"："曹操","刘备","孙权"
     "技术" ："曹操","刘备","张飞","关羽"
        1. 定义数据结构,存储以上信息.
        2. 是经理也是技术的都有谁?
        3. 是经理不是技术的都有谁?
        4. 不是经理是技术的都有谁?
        5. 身兼一职的都有谁?
        6. 公司总共有多少人数?
"""

set_manger = {"曹操", "刘备", "孙权"}
set_tec = {"曹操", "刘备", "张飞", "关羽"}

# 是经理也是技术的都有谁?
set_result = set_manger & set_tec
print(set_result)

# 是经理不是技术的都有谁?
set_result = set_manger - set_tec
print(set_result)

# 不是经理是技术的都有谁?
set_result = set_tec - set_manger
print(set_result)

# 身兼一职的都有谁?
set_result = set_manger ^ set_tec
print(set_result)

# 公司总共有多少人数?
print(len(set_manger | set_tec))
