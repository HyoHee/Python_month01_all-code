"""
    创建子类：狗(跑)，鸟类(飞)
          创建父类：动物(吃)
          体会子类复用父类方法
      体会 isinstance 、issubclass 与 type 的作用.
"""


class Animal:
    def eat(self):
        print("吃")


class Dog(Animal):
    def run(self):
        print("跑")
        self.eat()


class Brid(Animal):
    def fly(self):
        print("飞")


d01 = Dog()
d01.run()

b01 = Brid()
b01.fly()
b01.eat()

a01 = Animal()

print(isinstance(d01, Dog))
print(isinstance(b01, Dog))
print(isinstance(d01, Animal))
print(isinstance(a01, Dog))

print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))
print(issubclass(Brid, Animal))
print(issubclass(Dog, Brid))

print(type(d01) == Dog)
