"""
将一颗色子掷6000次，统计每种点数出现的次数

Author: CWP
Version: 1.0
"""
import random

f1, f2, f3, f4, f5, f6 = 0, 0, 0, 0, 0, 0
cnt = 6000
while cnt > 0:
    num = random.randrange(1, 7)
    match num:
        case 1: f1 += 1
        case 2: f2 += 1
        case 3: f3 += 1
        case 4: f4 += 1
        case 5: f5 += 1
        case _: f6 += 1
    cnt -= 1
print(f'1 = {f1}, 2 = {f2}, 3 = {f3}, 4 = {f4}, 5 = {f5}, 6 = {f6}')

items1 = [100, 1.23, 'Python', True]
print(items1)

items2 = list(range(1, 10))
items3 = list('hello world')
print(items2)
print(items3)

print(items2 + items1)
print(items2 * 2)

print(29 in items2)
print(4 in items2)
print(4 not in items2)

items4 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items4[4])
items4[4] = 'durian'
print(items4[4])
print(items4[-4])
print(items4[1:4:2])
print(items4[-2:-7:-1])
print(items4[:5:1])


languages = ['Python', 'Java', 'C++', 'Kotlin']
for _ in range(len(languages)):
    print(languages[_])
for _ in languages:
    print(_)

count = [0] * 6
for _ in range(6000):
    num = random.randrange(1, 7)
    count[num - 1] += 1
print(count)