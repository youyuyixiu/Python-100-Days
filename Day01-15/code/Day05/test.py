"""
找出所有水仙花数
"""
# for num in range(100,1000):
#     low = num % 10
#     mid = num // 10 % 10
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)

"""
正整数的翻转
"""
# num = int(input('num='))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num = num // 10
# print(reversed_num)

"""
百鸡百钱
"""
for x in range(0,20):
    for y in range(0,33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('%d只公鸡, %d只母鸡，%d只小鸡' %(x, y, z))

"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注
"""
from random import randint

money = 1000
while money > 0:
    print('你的总资产是：',money)
    needs_go_on = False
    while True:
        debt = int(input('请下注：'))
        if 0 < debt <= money:
            break
    first = randint(1,6) + randint(1,6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print('玩家赢')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家赢')
        money -= debt
    else:
        needs_go_on = True
        while needs_go_on:
            needs_go_on = False
            current = randint(1,6) + randint(1,6)
            print('玩家摇出了%d点' % current)
            if current == 7:
                print('庄家赢')
                money -= debt
            elif current == first:
                print('玩家赢')
                money += debt
            else:
                needs_go_on = True
print('you are broke')
        