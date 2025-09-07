"""
输出 100 以内的素数
素数指的是只能被 1 和自身整除的正整数（不包括 1）

Version 1.0
Author: CWP
"""
import random

for num in range(1, 101):
    is_prime = True
    for _ in range(2, int(num ** 0.5) + 1):
        if num % _ == 0:
            is_prime = False
            break
    if is_prime:
        print(num)


"""
输出斐波那契数列中的前20个数
波那契数列的特点是数列的前两个数都是 1，从第三个数开始，每个数都是它前面两个数的和。

Version 1.0
Author: CWP
"""
i, j = 0, 1
for _ in range(20):
    i, j = j, i + j
    print(i)

"""
找出 100 到 999 范围内的所有水仙花数。

提示：在数论中，水仙花数是一个 N 位非负整数，其各位数字的 N 次方和刚好等于该数本身对于三位数.

Version 1.0
Author: CWP
"""
for _ in range(100, 1000):
    a = _ % 10
    b = _ // 10 % 10
    c = _ // 100
    if _ == a ** 3 + b ** 3 + c ** 3:
        print(_)

"""
正整数的反转

Version: 1.0
Author: CWP
"""
num = 1238901
revers_num = 0
while num > 0:
    revers_num = revers_num * 10 + num % 10
    num //= 10
print(revers_num)

"""
百钱百鸡问题
说明：百钱百鸡是我国古代数学家张丘建在《算经》一书中提出的数学问题：
鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
翻译成现代文是：公鸡 5 元一只，母鸡 3 元一只，小鸡 1 元三只，用 100 块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？

Version: 1.0
Author: CWP
"""
for x in range(0, 21):
    for y in range(0, 34):
        z = 100 - x - y
        if z % 3 == 0 and 5*x + 3*y + z//3 == 100:
            print(f'公鸡: {x}只，母鸡: {y}只，小鸡: {z}只。')


"""
CRAPS赌博游戏
说明：该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。
简化后的规则是：玩家第一次摇骰子如果摇出了 7 点或 11 点，玩家胜；
玩家第一次如果摇出 2 点、3 点或 12 点，庄家胜；
玩家如果摇出其他点数则游戏继续，玩家重新摇骰子，如果玩家摇出了 7 点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数玩家继续摇骰子，直到分出胜负。
为了增加代码的趣味性，我们设定游戏开始时玩家有 1000 元的赌注，
每局游戏开始之前，玩家先下注，如果玩家获胜就可以获得对应下注金额的奖励，
如果庄家获胜，玩家就会输掉自己下注的金额。游戏结束的条件是玩家破产（输光所有的赌注）。

Version: 1.0
Author: CWP
"""
money = 1000
while money > 0:
    print(f'剩余资金{money}')
    while True:
        cur = int(input('请下本回合赌注'))
        if 0 < cur < money:
            break
        first_point = random.randrange(1, 13)
        print(first_point)
        if first_point == 7 or first_point == 11:
            print('恭喜你赢得本回合！')
            money += cur
            break
        elif first_point == 2 or first_point == 3 or first_point == 12:
            money -= cur
            print(f'庄家获胜，扣除{cur}赌注')
            break
        else:
            while True:
                cur_point = random.randrange(1, 13)
                if cur_point == first_point:
                    money += cur
                    print('恭喜你赢得本回合！')
                    break
                if cur_point == 7:
                    money -= cur
                    print(f'庄家获胜，扣除{cur}赌注')
                    break
print('你破产了！Game over！')


