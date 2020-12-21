"""
    将列表中所有元素转换为一个字符串
    列表:["我", "爱", "你", "p", "y", "t", "h", "o", "n", 666]
    结果:我爱你python666
"""

list_str = ["我", "爱", "你", "p", "y", "t", "h", "o", "n", 666]
list_temp = [str(item) for item in list_str]
result = "".join(list_temp)
print(result)
