"""
输入m和n，计算组合数C(m,n)的值

Version: 1.0
Author: CWP
"""
from math import factorial
from random import randrange

# m = int(input('m = '))
# n = int(input('n = '))
# fm = 1
# for num in range(1, m + 1):
#     fm *= num
# fn = 1
# for num in range(1, n + 1):
#     fn *= num
# fk = 1
# for num in range(1, m - n + 1):
#     fk *= num
#
# print(fm // (fn * fk))
#
#
# def fac(num):
#     res = 1
#     for _ in range(1, num + 1):
#         res *= _
#     return res
# print(fac(m) // (fac(n) * fac(m - n)))
#
# print(factorial(m) // factorial(n) // factorial(m - n))

def make_judgement(a, b, c):
    return a + b > c and b + c > a and a + c > b

print(make_judgement(4, 2, 3))
print(make_judgement(11, 56, 90))
print(make_judgement(c = 4, b = 3, a = 5))

def roll_dice(n = 2):
    total = 0
    for _ in range(n):
        total += randrange(1, 7)
    return total
print(roll_dice())
print(roll_dice(3))

def add(a = 0, b = 0, c = 0):
    return a + b + c

print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))

def add2(*args):
    total = 0
    for val in args:
        if type(val) in (int, float):
            total += val
    return total
print(add2())
print(add2(1))
print(add2(1, 2, 3))
print(add2(1, 2, 'hello', 3.45, 6))

def foo(*args, **kwargs):
    print(args)
    print(kwargs)

foo(3, 2.1, True, name='骆昊', age=43, gpa=4.95)


def foo():
    print('hello, world!')

def foo():
    print('goodbye, world!')

foo()