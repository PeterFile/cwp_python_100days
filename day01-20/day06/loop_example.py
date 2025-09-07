"""
循环结构练习

Version 1.0
Author: CWP
"""
import random

total = 0
for _ in range(1, 101):
    total += _
print(total)

total = 0
# for _ in range(2, 101, 2):
#     total += _
print(sum(range(2, 101, 2)))

# i = 1
# while i < 101:
#     total += i
#     i += 1
# print(total)

# i = 2
# while True:
#     total += i
#     i += 2
#     if i > 100:
#         break
# print(total)

for _ in range(1, 101):
    if _ % 2 != 0:
        continue
    else:
        total += _
print(total)

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{i} × {j} = {i * j}', end='\t')
#     print()


# num = int(input('请输入一个整数: '))
# end = int(num ** 0.5)
# is_prime = True
# for _ in range(2, end + 1):
#     if num % _ == 0:
#         is_prime = False
#         break
# if is_prime:
#     print(f'{num}是素数')
# else:
#     print(f'{num}不是素数')

# x = int(input('x = '))
# y = int(input('y = '))
# for _ in range(x, 0, -1):
#     if x % _ == 0 and y % _ == 0:
#         print(f'最大公约数是{_}')
#         break
# while y % x != 0:
#     x, y = y % x, x
# print(f'最大公约数：{x}')

num = random.randrange(1, 101)
cnt = 0
while True:
    i = int(input('i = '))
    cnt += 1
    if i < num:
        print('大一点')
    elif i > num:
        print('小一点')
    else:
        print(f'猜对了，你一共猜了{cnt}次')