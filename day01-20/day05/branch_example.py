"""
BMI 计算器

Version 1.0
Author: CWP
"""

height = float(input('身高(cm): '))
weight = float(input('体重(kg): '))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')
if bmi < 18:
    print('你的身材过轻！')
elif bmi < 24:
    print('你的身材很棒！')
elif bmi < 27:
    print('你的身材过重！')

status_code = int(input('响应状态码：'))
match status_code:
    case 400 | 405: desc = 'Invalid Request'
    case 401: desc = 'Unauthorized'
    case 403: desc = 'Forbidden'
    case 404: desc = 'Not Found'
    case _: desc = 'Unknow Status Code'
print('状态码描述：', desc)

x = int(input('请输入x: '))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'{y = }')

score = float(input('请输入你的成绩：'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f'{grade}')

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    print(f'周长: {perimeter}')
    s = perimeter / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print(f'面积：{area}')
else:
    print('不能构成三角形')