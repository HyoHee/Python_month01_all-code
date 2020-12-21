"""
    创建函数,根据课程阶段计算课程名称
"""


def get_course_level(level):
    """
        根据课程阶段查找课程名称
    :param level: 课程阶段数，str类型
    :return: 课程名称，str类型
    """
    dict_level = {
        "1": "Python语言核心编程",
        "2": "Python高级软件技术",
        "3": "Web全栈",
        "4": "网络爬虫",
        "5": "数据分析、人工智能"
    }
    if level in dict_level:
        return dict_level[level] # 如果键不存在自动返回None

number = input("请输入课程阶段数：")
print(get_course_level(number))
