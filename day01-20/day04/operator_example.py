"""
算术运算符

Version: 1.0
Author: CWP
"""
import math

print(9 // 4)
print(9 ** 3)

print((a := 10))
b = 3
a += b
a *= a + 2
print(a)
print(15 * 13)

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = not flag0
flag4 = flag1 and flag2
flag41 = flag1 | flag2
flag5 = flag1 or flag2

print(flag0)
print(flag1)
print(flag2)
print(flag3)
print(flag4)
print(flag41)
print(flag5)

f = float(input('请输入华氏温度：'))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')

radius = float(input('请输入圆的半径：'))
perimeter = math.pi * 2 * radius
area = math.pi * radius * radius
print(f'{perimeter = :.2f}; {area = :.2f}')

year = int(input('请输入年份：'))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(f'{is_leap = }')