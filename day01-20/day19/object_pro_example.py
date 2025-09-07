# class Student:
#     # 通过'__slots__'指定类属性
#     __slots__ = ('__name', '__age')
#
#     def __init__(self, name, age):
#         """
#         通过'__'标识一个私有属性，'_'标识一个受保护属性
#         :param name:
#         :param age:
#         """
#         self.__name = name
#         self.__age = age
#
#     def study(self, course_name):
#         print(f'{self.__name}正在学习{course_name}')
#
# stu = Student('王大锤', 20)
# stu.study('Python程序设计')
# print(stu._Student__name)

# 动态添加属性
# stu.sex = '男'

class Triangle(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    """ 
    'staticmethod'装饰器声明静态方法，'classmethod'声明类方法，都可以直接使用 类名.方法 来调用，
    区别在于类方法第一个参数是类对象本身，静态方法没有这个参数
    """
    @staticmethod
    def is_valid(a, b, c):
        """判断三边能否构成三角形(静态方法)"""
        return a + b > c and a + c > b and b + c > a

    # @classmethod
    # def is_valid(cls, a, b, c):
    #     """判断三边能否构成三角形(静态方法)"""
    #     return a + b > c and a + c > b and b + c > a

    """ property 装饰器可以让方法变成两个属性，不再通过调用方法的方式来访问，而是用访问属性的方式直接获得 """
    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.05

t = Triangle(3, 4, 5)
print(f'周长 = {t.perimeter}')
print(f'面积 = {t.area}')

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}正在吃饭.')

    def sleep(self):
        print(f'{self.name}正在睡觉.')
"""继承的语法是在定义类的时候，在类名后的圆括号中指定当前类的父类。"""
class Student(Person):

    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')

class Teacher(Person):

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')

stu1 = Student('白元芳', 21)
stu2 = Student('狄仁杰', 22)
tea1 = Teacher('武则天', 35, '副教授')
stu1.eat()
stu2.sleep()
tea1.eat()
stu1.study('Python程序设计')
tea1.teach('Python程序设计')
stu2.study('数据科学导论')