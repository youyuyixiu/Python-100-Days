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
输入一个正整数判断它是不是素数
"""
