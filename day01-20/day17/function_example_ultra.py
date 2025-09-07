import random
import time
from functools import wraps, lru_cache


def record_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        return result
    return wrapper

@record_time
def download(filename):
    """下载文件"""
    print(f'开始下载{filename}')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')

@record_time
def upload(filename):
    """上传文件"""
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')

# download('MySQL从删库到跑路.avi')
# upload('Python从入门到住院.pdf')
# download.__wrapped__('MySQL必知必会.pdf')
@lru_cache()
def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)

start1 = time.time()
for i in range(1, 51):
    print(fib1(i))
end1 = time.time()
print(f'执行时间: {end1 - start1:.2f}秒')
def fib2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
for i in range(1, 21):
    print(fib2(i))