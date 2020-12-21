"""
    画出下列代码的内存图，说出终端显示结果
"""
name_of_beijing, regin = "北京", "市"
name_of_beijing_regin = name_of_beijing + regin
regin = "省"
print(name_of_beijing_regin)
del name_of_beijing
print(name_of_beijing_regin)
