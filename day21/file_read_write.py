# file = open('致橡树.txt', 'a', encoding='utf-8')
# for line in file:
#     print(line, end='')
#
# file.write('\n标题：《致橡树》')
# file.write('\n作者：舒婷')
# file.write('\n时间：1977年3月')

# file1 = None
# try:
#     file1 = open('致橡树.txt', 'r', encoding='utf-8')
#     print(file1.read())
# except FileExistsError:
#     print('无法打开指定的文件！')
# except LookupError:
#     print('指定了未知的编码！')
# except UnicodeDecodeError:
#     print('读取文件时解码错误！')
# finally:
#     if file1:
#         file1.close()
#
# class InputError(ValueError):
#     pass
#
# def fac(num):
#     if num < 0:
#         raise InputError('只能计算非负整数的阶乘')
#     if num in (0, 1):
#         return 1
#     return num * fac(num - 1)
#
# flag = True
# while flag:
#     num = int(input('n = '))
#     try:
#         print(f'{num}! = {fac(num)}')
#         flag = False
#     except InputError as err:
#         print(err)

try:
    with open('guido.jpg', 'rb') as file1:
        data = file1.read()
    with open('吉多.jpg', 'wb') as file2:
        file2.write(data)
except FileNotFoundError:
    print('指定的文件无法打开.')
except IOError:
    print('读写文件时出现错误.')
print('程序执行结束.')

try:
    with open('guido.jpg', 'rb') as file1, open('吉多.jpg', 'wb') as file2:
        data = file1.read(512)
        while data:
            file2.write(data)
            data = file1.read()
except FileNotFoundError:
    print('指定的文件无法打开.')
except IOError:
    print('读写文件时出现错误.')
print('程序执行结束.')