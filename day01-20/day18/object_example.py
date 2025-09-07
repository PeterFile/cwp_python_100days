import time


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}学生正在学习{course_name}')

    def play(self):
        print(f'{self.name}学生正在玩游戏')

stu1 = Student('小陈', 24)
stu2 = Student('达维', 25)
print(stu1)
print(stu2)

Student.study(stu1, 'Python')
stu1.study('Python')

Student.play(stu2)
stu2.play()

class Clock:

    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.min = minute
        self.sec = second

    def run(self):
        self.sec += 1
        if self.sec == 60:
            self.min += 1
            self.sec = 0
            if self.min == 60:
                self.min = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'

clock = Clock(23, 59, 58)
# while True:
#     print(clock.show())
#     time.sleep(1)
#     clock.run()


class Point:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance_to(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx * dx + dy * dy) ** 0.5

    def __str__(self):
        return f'({self.x}, {self.y})'

p1 = Point(3, 5)
p2 = Point(6, 9)
print(p1)
print(p2)
print(p1.distance_to(p2))