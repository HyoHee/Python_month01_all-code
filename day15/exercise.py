"""
    模块调用
"""

import module_exercise

print(module_exercise.data)

e01=module_exercise.MyClass()
e01.func02()
module_exercise.func01()

module_exercise.MyClass.func03()


from module_exercise import *

print(data)

func01()

MyClass.func03()
e01=MyClass()
e01.func02()