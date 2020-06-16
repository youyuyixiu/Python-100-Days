"""
用for循环实现1~100求和
"""
# sum = 0
# for x in range(1,101):
#     sum += x
# print(sum)

"""
用for循环实现1~100偶数求和
"""
# sum = 0
# for x in range(2,101,2):
#     sum += x
# print(sum)

"""
用for循环实现1~100偶数求和
"""
# sum = 0
# for x in range(1,101):
#     if x % 2 == 0:
#         sum += x
# print(sum)

"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
# import random

# answer = random.randint(1,100)
# count = 0

# while True:
#     count += 1
#     number = int(input('请输入数字：'))
#     if number < answer:
#         print('猜小了')
#     elif number > answer:
#         print('猜大了')
#     else:
#         print('猜对了')
#         break
# print('您总共猜了%d次' % count)
# if count > 7:
#     print('您的智商需要及时充值')

"""
输出乘法口诀表(九九表)
"""
# for i in range(1,10):
#     for j in range(1, i+1):
#         print('%d*%d=%d' %(j, i, i*j), end='\t')
#     print()

"""
ex1 输入一个正整数判断它是不是素数
"""
# from math import sqrt
# num = int(input('请输入正整数：'))
# is_prime = True
# end = int(sqrt(num))
# print(end)
# for i in range(2, end+1):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime == True and num != 1:
#     print('%d是素数' % (num))
# else:
#     print('%d不是素数' % (num))

"""
ex2 输入两个正整数计算它们的最大公约数和最小公倍数
"""
# x = int(input('请输入正整数：'))
# y = int(input('请输入正整数：'))
# if x > y:
#     x, y = y, x
# for i in range(x, 0, -1):
#     if x % i == 0 and y % i == 0:
#         print('最大公约数为%d' % i)
#         print('最小公倍数为%d' % (x*y//i))
#         break

"""
ex3 打印三角形图案
"""
# row = int(input('请输入行数：'))
# for i in range(row):
#     for j in range(i+1):
#         print('*',end='')
#     print()

# row = int(input('请输入行数：'))
# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()

row = int(input('请输入行数：'))
for i in range(row):
    for j in range(row - i -1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()