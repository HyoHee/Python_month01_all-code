"""
    小明使用手机打电话
    要求:增加座机,卫星电话时不影响小明.
"""


class Person:
    def __init__(self, name=""):
        self.name = name

    def use(self, tool):
        print("使用")
        tool.call()


class CommunicationTool:
    def call(self):
        pass


class Phone(CommunicationTool):
    def call(self):
        print("手机打电话")

class Telephone(CommunicationTool):
    def call(self):
        print("座机打电话")

class SatellitePhone(CommunicationTool):
    def call(self):
        print("卫星电话打电话")
