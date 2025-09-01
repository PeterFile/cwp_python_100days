"""
设计一个生成随机验证码的函数，验证码由数字和英文大小写字母构成，长度可以通过参数设置。

Author: CWP
Version: 1.0
"""
import random
import string

ALL_CHARS = string.digits + string.ascii_letters

def generate_code(*, code_len = 4):
    return ''.join(random.choices(ALL_CHARS, k=code_len))

for _ in range(5):
    print(generate_code(code_len=8))


"""
判断素数。

Author: CWP
Version: 1.0
"""
def is_prime(num: int) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for _ in {14, 634, 63463,421}:
    print(is_prime(_))

"""
最大公约数和最小公倍数。

Author: CWP
Version: 1.0
"""
def lcm(x: int, y: int) -> int:
    return x * y // gcd(x, y)

def gcd(x: int, y: int) -> int:
    while y % x != 0:
        x, y = y % x, x
    return x

"""
数据统计

Author: CWP
Version: 1.0
"""
def ptp(data):
    """极差"""
    return max(data) - min(data)

def mean(data):
    """算术平均"""
    return sum(data) / len(data)

def median(data):
    """中位数"""
    temp, size = sorted(data), len(data)
    if size % 2 != 0:
        return temp[size // 2]
    else:
        return mean(temp[size // 2 - 1:size // 2 + 1])

def var(data, ddof=1):
    """方差"""
    x_bar = mean(data)
    temp = [(num - x_bar) ** 2 for num in data]
    return sum(temp) / (len(temp) - ddof)

def std(data, ddof=1):
    """标准差"""
    return var(data, ddof) ** 0.5

def cv(data, ddof=1):
    """变异系数"""
    return std(data, ddof) / mean(data)

def describe(data):
    """输出描述性统计信息"""
    print(f'均值: {mean(data)}')
    print(f'中位数: {median(data)}')
    print(f'极差: {ptp(data)}')
    print(f'方差: {var(data)}')
    print(f'标准差: {std(data)}')
    print(f'变异系数: {cv(data)}')

describe({1,6,42,6234,622,5535,211,5523})

"""
双色球随机选号程序

Author: CWP
Version: 1.3
"""
RED_BALLS = [i for i in range(1, 34)]
BLUE_BALLS = [i for i in range(1, 17)]

def choose():
    """
    生成一组随机号码
    :return: 保存随机号码的列表
    """
    selected_balls = random.sample(RED_BALLS, 6)
    selected_balls.sort()
    selected_balls.append(random.choice(BLUE_BALLS))
    return selected_balls

def display(balls):
    """
    格式输出一组号码
    :param balls: 保存随机号码的列表
    """
    for ball in balls[:-1]:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    print(f'\033[034m{balls[-1]:0>2d}\033[0m')

n = int(input('生成几注号码: '))
for _ in range(n):
    display(choose())