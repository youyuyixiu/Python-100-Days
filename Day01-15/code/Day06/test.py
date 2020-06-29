"""
输入M和N计算C(M,N)
"""
# m = int(input('m= '))
# n = int(input('n= '))
# fm = 1
# for num in range(1, m+1):
#     fm *= num
# fn = 1
# for num in range(1, n+1):
#     fn *= num
# fmn = 1
# for num in range(1, m-n+1):
#     fmn *= num
# print(fm // fn // fmn)

"""
重构代码
"""
# def factorial(num):
#     result = 1
#     for n in range(1, num + 1):
#         result *= n
#     return result

# m = int(input('m= '))
# n = int(input('n= '))
# print(factorial(m) // factorial(n) // factorial(m-n))

"""
函数的参数
"""

# from random import randint

# def roll_dice(n=2):
#     """摇色子"""
#     total = 0
#     for _ in range(n):
#         total += randint(1, 6)
#     return total

# def add(a=0, b=0, c=0):
#     return a+b+c

# print(roll_dice())
# print(roll_dice(2))
# print(roll_dice(3))

# print(add())
# print(add(1))
# print(add(1,2))
# print(add(1,2,3))
# print(add(c=3, b=2, a=1))


# def add(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# print(add())
# print(add(1))
# print(add(1,2))
# print(add(1,2,3))

"""
练习1：实现计算求最大公约数和最小公倍数的函数。
"""
# def gcd(a, b):
#     (a, b) = (b, a) if a > b else (a, b)
#     for num in range(a, 0, -1):
#         if a % num == 0 and b % num == 0:
#             return num

# def lcm(a, b):
#     return a * b // gcd(a, b)

# print(gcd(4,6))
# print(lcm(4,6))

