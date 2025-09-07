import random

from rich.console import Console
from rich.table import Table

languages = ['Python', 'C++', 'Golang']
languages.append('Java')
print(languages)
languages.insert(1, 'JavaScript')
print(languages)

if 'JavaScript' in languages:
    languages.remove('JavaScript')
print(languages)
languages.pop()
print(languages)
temp = languages.pop(1)
print(temp)
languages.append(temp)
print(languages)
languages.clear()
print(languages)
languages.append('Python')
languages *= 3
print(languages)
languages.remove('Python')
print(languages)

items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
print(items.index('Python', 1))
print(items.count('Python'))
items.sort()
print(items)
items.reverse()
print(items)

"""
创建一个取值范围在1到99且能被3或者5整除的数字构成的列表。

Author: CWP
Version: 1.0
"""
nums1 = []
for _ in range(1, 100):
    if _ % 3 == 0 or _ % 5 == 0:
        nums1.append(_)
print(nums1)

nums2 = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(nums2)

"""
有一个整数列表nums1，创建一个新的列表nums2，nums2中的元素是nums1中对应元素的平方。

Author: CWP
Version: 1.0
"""
nums3 = [23,47,865,142,5]
nums4 = []
for num in nums3:
    nums4.append(num ** 2)
print(nums3)
print(nums4)

nums5 = [i ** 2 for i in nums3]
print(nums5)

nums6 = [num for num in nums3 if num > 50]
print(nums6)

scores = [[random.randrange(0, 101) for _ in range(3)] for _ in range(5)]
print(scores)

"""
双色球随机选号程序

Author: CWP
Version: 1.0
"""
red_balls = list(range(1, 34))
selected_balls = []
for _ in range(6):
    index = random.randrange(len(red_balls))
    selected_balls.append(red_balls.pop(index))
selected_balls.sort()
for ball in selected_balls:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
blue_ball = random.randrange(1, 17)
print(f'\033[034m{blue_ball:0>2d}\033[0m')


console = Console()
red_balls1 = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]
n = int(input('生成几注号码：'))

table = Table(show_header=True)
for col in ('序号', '红球', '蓝球'):
    table.add_column(col, justify='center')

for _ in range(n):
    selected_balls1 = random.sample(red_balls1, 6)
    selected_balls1.sort()
    blue_ball1 = random.choice(blue_balls)
    table.add_row(
        str(_ + 1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'
    )

console.print(table)