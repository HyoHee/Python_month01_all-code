"""
     以面向对象的思想,描述下列情景.
        需求：小明使用手机打电话
"""


class Person:
    def __init__(self, name=""):
        self.name = name


    def use(self,mobilephone):
        print("使用")
        mobilephone.call()


class Phone:
    def call(self):
        print("打电话")
