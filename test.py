"""
day01--初始python
"""
# import this

# import turtle
# turtle.pensize(4)
# turtle.pencolor('red')
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.forward(100)
# turtle.mainloop()

"""
day02--语言元素
"""
# a = 321
# b = 123
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

# a = 100
# b = 12.345
# c = 1 + 5j
# d = 'hello, world'
# e = True
# print(type(a)) # <class 'int'>
# print(type(b)) # <class 'float'>
# print(type(c)) # <class 'complex'>
# print(type(d)) # <class 'str'>
# print(type(e)) # <class 'bool'>

# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))

# a = 10
# b = 3
# a += b
# a *= a + 2
# print(a)

# flag0 = 1 == 1
# flag1 = 3 > 2
# flag2 = 2 < 1
# flag3 = flag1 and flag2
# flag4 = flag1 or flag2
# flag5 = not (1 != 2)
# print('flag0 =', flag0) # flag0 = True
# print('flag1 =', flag1) # flag1 = True
# print('flag2 =', flag2) # flag2 = False
# print('flag3 =', flag3) # flag3 = False
# print('flag4 =', flag4) # flag4 = True
# print('flag5 =', flag5) # flag5 = False
# print(flag1 is True) # True
# print(flag2 is not False) # False

# str1 = 'hello, world!'
# print('字符串的长度是:', len(str1))
# print('单词首字母大写: ', str1.title())
# print('字符串变大写: ', str1.upper())
# # str1 = str1.upper()
# print('字符串是不是大写: ', str1.isupper())
# print('字符串是不是以hello开头: ', str1.startswith('hello'))
# print('字符串是不是以hello结尾: ', str1.endswith('hello'))
# print('字符串是不是以感叹号开头: ', str1.startswith('!'))
# print('字符串是不是一感叹号结尾: ', str1.endswith('!'))
# str2 = '- \u9a86\u660a'
# str3 = str1.title() + ' ' + str2.lower()
# print(str3)

# ex1：华氏温度转摄氏温度
# f = float(input('请输入华氏温度：'))
# c = (f - 32) / 1.8
# print('%.1f 华氏温度 = %.1f 摄氏温度' %(f, c))

# ex2: 计算圆的周长和面积
# import math
# radius = float(input('请输入圆的半径：'))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius * radius
# print('圆的周长是%.1f' % perimeter)
# print('圆的面积是%.1f' % area)

# ex3: 判断是否是闰年
# year = int(input('请输入年份：'))
# is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
# print(is_leap)

"""
day03--分支结构
"""
# 用户身份验证
# username = input('请输入用户名：')
# password = input('请输入密码：')
# if username == 'admin' and password == '123456':
#     print('身份验证成功')
# else:
#     print('身份验证失败')

# 分段函数求值
# x = float(input('x = '))
# if x > 1:
#     y = 3 * x - 5
# elif x >= -1:
#     y = x + 2
# else:
#     y = 5 * x + 3
# print('f(%.2f) = %.2f' % (x,y))

# x = float(input('x = '))
# if x > 1:
#     y = 3 * x - 5
# else:
#     if x >= -1:
#       y = x + 2
#     else:
#       y = 5 * x + 3
# print('f(%.2f) = %.2f' % (x, y))

# ex1:英寸和厘米转换
# value = float(input('请输入长度：'))
# unit = input('请输入单位：')
# if unit == 'in' or unit == '英寸':
#     print('%f英寸 = %f厘米' % (value, value * 2.54))
# elif unit == 'cm' or unit == '厘米':
#     print('%f英寸 = %f厘米' % (value, value / 2.54))
# else:
#     print('请输入正确的单位')

# ex2:百分制转换为等级制
# score = float(input('请输入成绩：'))
# if score >= 90:
#     grade = 'A'
# elif score >= 80:
#     grade = 'B'
# elif score >= 70:
#     grade = 'C'
# elif score >= 60:
#     grade = 'D'
# else:
#     grade = 'E'
# print('对应的等级是：', grade)

# ex3:计算三角形的周长和面积
# a = float(input('a = '))
# b = float(input('b = '))
# c = float(input('c = '))
# if a + b > c and a + c > b and b + c > a:
#     print('周长：%f' % (a + b + c))
#     p = (a + b + c) / 2
#     area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
#     print('面积：%f' % (area))
# else:
#     print('不能构成三角形')

"""
day04--循环结构
"""
# # for循环实现1~100求和
# sum = 0
# for x in range(101):
#     sum += x
# print(sum)

# # for循环实现1~100之间偶数求和
# sum = 0
# for x in range(2, 101, 2):
#     sum += x
# print(sum)

# # for循环实现1~100之间偶数求和(循环套分支)
# sum = 0
# for x in range(2, 101):
#     if x % 2 == 0:
#         sum += x
# print(sum)

# # 猜数字
# import random
# answer = random.randint(1,100)
# counter = 0
# while True:
#     counter += 1
#     number = int(input('请输入：'))
#     if number > answer:
#         print('猜大了')
#     elif number < answer:
#         print('猜小了')
#     else:
#         print('猜对了')
#         break  
# print('您总共猜了%d次' % counter)
# print('正确答案是%d' % answer)
# if counter > 7:
#     print('您的智商明显不足')

# # 99乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('%d*%d=%d' %(i, j, i*j), end='\t')
#     print()

# # ex1:判断一个正整数是不是素数
# from math import sqrt
# num = int(input('请输入正整数：'))
# end = int(sqrt(num))
# is_prime = True
# for i in range(2, end + 1):
#     if num % i == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num)
# else:
#     print('%d不是素数' % num)

# # ex2:求两个正整数的最大公约数和最小公倍数
# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
#     x, y = y, x
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d和%d的最大公约数是%d' % (x, y, factor))
#         print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
#         break

# row = int(input('请输入行数：'))
# for i in range(row):
#     for _ in range(i+1):
#         print('*', end='')
#     print()

# row = int(input('请输入行数：'))
# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()

# row = int(input('请输入行数：'))
# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()

# row = int(input('请输入行数：'))
# for i in range(row):
#     for _ in range(row - i -1):
#         print(' ',end='')
#     for _ in range(2 * i + 1):
#         print('*',end='')
#     print()

"""
day05--构造程序逻辑
"""

# # 水仙花数
# for i in range(100, 1000):
#     low = i % 10
#     mid = i // 10 % 10
#     high = i // 100
#     if (i == low ** 3 + mid ** 3 + high ** 3):
#         print(i)

# # 正整数的反转
# num = int(input('num = '))
# reverse_num = 0
# while num > 0:
#     reverse_num = reverse_num * 10 + num % 10
#     num //= 10
# print(reverse_num)

# # 百钱百鸡(暴力搜索法)
# for i in range(0, 20):
#     for j in range(0, 33):
#         k = 100 - i - j
#         if i * 5 + j * 3 + k / 3 == 100:
#             print('公鸡%d只，母鸡%d只，小鸡%d只' % (i, j, k))

# # 赌博游戏
# from random import randint

# money = 1000
# while money > 0:
#     print('你的总资产为:', money)
#     needs_go_on = False
#     while True:
#         debt = int(input('请下注: '))
#         if 0 < debt <= money:
#             break
#     first = randint(1, 6) + randint(1, 6)
#     print('玩家摇出了%d点' % first)
#     if first == 7 or first == 11:
#         print('玩家胜!')
#         money += debt
#     elif first == 2 or first == 3 or first == 12:
#         print('庄家胜!')
#         money -= debt
#     else:
#         needs_go_on = True
#     while needs_go_on:
#         needs_go_on = False
#         current = randint(1, 6) + randint(1, 6)
#         print('玩家摇出了%d点' % current)
#         if current == 7:
#             print('庄家胜')
#             money -= debt
#         elif current == first:
#             print('玩家胜')
#             money += debt
#         else:
#             needs_go_on = True
# print('你破产了, 游戏结束!')

# # fibonacci
# a = 0
# b = 1
# for _ in range(20):
#     a, b = b, a+b
#     print(a, end=' ')

# # perfect
# import math
# for num in range(1, 10000):
#     result = 0
#     for factor in range(1, int(math.sqrt(num))+1):
#         if num % factor == 0:
#             result += factor
#             if factor > 1 and num // factor != factor:
#                 result += num // factor
#     if result == num:
#         print(num)

# # prime
# import math
# for num in range(2,100):
#     is_prime = True
#     for factor in range(2, int(math.sqrt(num))+1):
#         if num % factor == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num,end=' ')

"""
day06--函数和模块
"""
# # 计算C(M,N)
# import math
# m = int(input('m= '))
# n = int(input('n= '))
# fm = 1
# for num in range(1,m+1):
#     fm *= num
# fn = 1
# for num in range(1,n+1):
#     fn *= num
# fmn = 1
# for num in range(1,m-n+1):
#     fmn *= num
# print(fm // fn // fmn)

# 函数计算C(M,N)
# def factorial(num):
#     result = 1
#     for n in range(1, num+1):
#         result *= n
#     return result

# m = int(input('m= '))
# n = int(input('n= '))
# print(factorial(m) // factorial(n) // factorial(m-n))

# 函数参数
# from random import randint
# def roll_dice(n=2):
#     total = 0
#     for _ in range(n):
#         total += randint(1,6)
#     return total

# def add(a=0, b=0, c=0):
#     return a + b + c

# print(roll_dice())
# print(roll_dice(3))
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(c=3, b=2, a=1))

# # 可变参数
# def add(*args):
#     total = 0
#     for val in args:
#         total += val
#     return total

# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
# print(add(1, 3, 5, 7, 9))

# python没有函数重载，用module可以避免这种情况
# def foo():
#     print('hello')

# def foo():
#     print('goodbye')

# foo()

# def foo():
#     pass

# def bar():
#     pass

# # __name__是Python中一个隐含的变量它代表了模块的名字
# # 只有被Python解释器直接执行的模块的名字才是__main__
# # 导入module时 不会执行模块中if条件成立时的代码 因为模块的名字是module而不是__main__
# if __name__ == '__main__':
#     print('call foo()')
#     foo()
#     print('call bar()')
#     bar()

# # ex1: gcd lcm
# def gcd(x, y):
#     (x, y) = (y, x) if x > y else (x, y)
#     for factor in range(x, 0, -1):
#         if x % factor == 0 and y % factor == 0:
#             return factor

# def lcm(x, y):
#     return x * y // gcd(x, y)

# print(gcd(8, 12))
# print(lcm(8, 12))

# # ex2：palindrome
# def is_palindrome(num):
#     total = 0
#     temp = num
#     while temp > 0:
#         total = total * 10 + temp % 10
#         temp //= 10
#     return total == num

# # print(is_palindrome(12321))

# # ex3: prime
# def is_prime(num):
#     for factor in range(2, num):
#         if num % factor == 0:
#             return False
#     return True if num != 1 else False

# # print(is_prime(3))

# ex4:回文素数
# if __name__ == '__main__':
#     num = int(input('请输入正整数：'))
#     if is_prime(num) and is_palindrome(num):
#         print('%d是回文素数' % num)
#     else:
#         print('%d不是回文素数' % num)

# # 全局变量
# def foo():
#     b = 'hello'

#     def bar():
#         c = True
#         print(a)
#         print(b)
#         print(c)
    
#     bar()       

# if __name__ == '__main__':
#     a = 100
#     foo()

# # 注意局部变量a和全局变量a的不同
# def foo():
#     a = 200
#     print(a)

# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)

# global
# def foo():
#     global a
#     a = 200
#     print(a)

# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)

# def main():
#     pass

# if __name__ == '__main__':
#     main()

"""
day07--字符串和常用的数据结构
"""
# s1 = 'hello world'
# s2 = "hello world"
# s3 = """
# hello world
# hello python
# """
# print(s1, s2, s3, end='')

# s1 = '\'hello world\''
# s2 = '\n\\hello world\\\n'
# print(s1, s2, end='')

# s1 = '\141\142\143\x61\x62\x63'
# s2 = '\u9a86\u660a'
# print(s1, s2)

# s1 = r'\'hello world\''
# s2 = r'\n\\hello world\\\n'
# print(s1, s2, end='')

# s1 = 'hello' * 3
# print(s1)
# s2 = 'world'
# s1 += s2
# print(s1)
# print('ll' in s1)
# print('good' in s1)
# str = 'abc123456'
# print(str[2])
# print(str[2:5])
# print(str[2::2])
# print(str[::2])
# print(str[::-1])
# print(str[-3:-1])

# str = 'hello, world'
# print(len(str))
# print(str.capitalize())
# print(str.title())
# print(str.find('or'))
# print(str.find('shit'))
# print(str.index('or'))
# # print(str.index('shit'))
# print(str.startswith('He'))
# print(str.startswith('he'))
# print(str.endswith('ld'))
# print(str.center(50, '*'))
# print(str.rjust(50, ' '))
# print(str.isdigit())
# print(str.isalpha())
# print(str.isalnum())
# str2 = '  xiaoshuyi123@163.com  '
# print(str2.strip())

# a, b = 1, 2
# print('%d * %d = %d' % (a, b, a*b))
# print('{0} * {1} = {2}'.format(a, b, a*b))
# print(f'{a} * {b} = {a * b}')

# # list
# list1 = [1, 3, 5, 7, 100]
# print(list1)
# list2 = ['hello'] * 3
# print(list2)
# print(len(list1))
# print(list1[0])
# print(list1[4])
# print(list1[-1])
# print(list1[-3])
# list1[2] = 300
# print(list1)
# for index in range(len(list1)):
#     print(list1[index])
# for elem in list1:
#     print(elem)
# for index,elem in enumerate(list1):
#     print(index, elem)

# list1 = [1,3,5,7,100]
# list1.append(200)
# list1.insert(1,400)
# # print(list1)
# # list1.extend([1000,2000])
# # print(list1)
# list1 += [1000,2000]
# # print(list1)
# if 3 in list1:
#     list1.remove(3)
# if 1234 in list1:
#     list1.remove(1234)
# # print(list1)
# list1.pop(0)
# list1.pop(len(list1) - 1)
# # print(list1)
# list1.clear()
# print(list1)

# fruits = ['a', 'b', 'c', 'd']
# fruits += ['e', 'f', 'g']
# fruits2 = fruits[1:4]
# print(fruits2)
# fruits3 = fruits[:]
# print(fruits3)
# fruits4 = fruits[::-1]
# print(fruits4)
# fruits5 = fruits[-3:-1]
# print(fruits5)

# list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# list2 = sorted(list1)
# list3 = sorted(list1, reverse=True)
# list4 = sorted(list1, key = len)
# print(list1)
# print(list2)
# print(list3)
# print(list4)
# list1.sort(reverse=True)
# print(list1)

# 生成式和生成器
import sys
# f = [x for x in range(1, 10)]
# print(f)
# f = [x + y for x in 'ABCDE' for y in '1234567']
# print(f)
# f = [x ** 2 for x in range(1, 1000)]
# print(sys.getsizeof(f))
# print(f)

# f = (x ** 2 for x in range(1, 1000))
# print(sys.getsizeof(f))
# for val in f:
#     print(val)

# def fib(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a+b
#         yield a
# def main():
#     for val in fib(20):
#         print(val)

# if __name__ == '__main__':
#     main()

# # tuple
# t = ('xsy', 27, True, '济南')
# print(t)
# print(t[0])
# print(t[3])
# for member in t:
#     print(member)
# t = ('xiao', 'shu', 'yi')
# print(t)
# person = list(t)
# print(person)
# person[0] = 'hello'
# print(person)
# fruit_list = ['apple', 'banana', 'orange']
# fruit_tuple = tuple(fruit_list)
# print(fruit_tuple)

# list = [1,2,3,4,5]
# tuple = (1,2,3,4,5)
# print(sys.getsizeof(list))
# print(sys.getsizeof(tuple))

# # set
# set1 = {1,2,3,3,2,1}
# print(set1)
# print(len(set1))
# set2 = set(range(1,10))
# set3 = set((1,2,3,3,2,1))
# print(set2,set3)
# set4 = {num for num in range(1,100) if num % 3 == 0 or num % 5 == 0}
# print(set4)

# set1.add(4)
# set1.add(5)
# set2.update([11,12])
# set2.discard(5)
# if 4 in set2:
#     set2.remove(4)
# print(set1, set2)
# print(set3)
# print(set3.pop())
# print(set3.pop())
# print(set3.pop())
# print(set3)
# print(set1 & set2)
# print(set1 | set2)
# print(set1 - set2)
# print(set1 ^ set2)
# print(set2 <= set1)
# print(set3 <= set1)
# print(set1 >= set2)
# print(set1 >= set3)

# # dict
# scores = {'xiao':1, 'shu':2, 'yi':3}
# items1 = dict(one=1, two=2, three=3, four=4)
# items2 = dict(zip(['a', 'b', 'c'], '123'))
# items3 = {num:num ** 2 for num in range(1,10)}
# print(items1, items2, items3)
# print(scores)
# print(scores['xiao'])
# for key in scores:
#     print(f'{key}:{scores[key]}')
# scores['xsy'] = 4
# scores.update(youyuyixiu=5)
# print(scores)
# print(scores.get('xiao'))
# print(scores.get('wang',10))
# print(scores)
# print(scores.popitem())
# print(scores.popitem())
# print(scores.pop('xiao'))
# print(scores)
# print(scores.clear())
# print(scores)

# # ex1:跑马灯
# import os
# import time

# def main():
#     content = '北京欢迎你为你开天辟地......'
#     while True:
#         os.system('cls')
#         print(content)
#         time.sleep(0.2)
#         content = content[1:] + content[0]

# if __name__ == '__main__':
#     main()

# ex2:产生指定长度的验证码

# import random

# def generate_code(code_len = 4):
#     """
#     生成指定长度的验证码
#     :param code_len:验证码的长度（默认4个字符）
#     :return:由大小写英文字母和数字构成的随机验证码
#     """
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0,len(all_chars)-1)
#         code += all_chars[index]
#     return code

# if __name__ == '__main__':
#     print(generate_code(10))

# # ex3:返回文件名的后缀名

# def get_suffix(filename, has_dot = False):
#     """
#     返回文件名的后缀名
#     :param filename: 文件名
#     :param has_dot: 返回的后缀名是否需要带点
#     :return: 文件的后缀名
#     """
#     pos = filename.rfind('.')
#     if 0 < pos < len(filename) - 1:
#         index = pos if has_dot else pos + 1
#         return filename[index:]
#     else:
#         return ''

# if __name__ == '__main__':
#     print(get_suffix('helloworld.txt', True))

# # ex4:返回列表中最大和次大的数

# def get_max2(x):
#     """
#     返回list的最大值和次大值
#     :param:传入的list
#     :return:返回最大值和次大值
#     """
#     m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
#     for i in range(2,len(x)):
#         if x[i] > m1:
#             m2 = m1
#             m1 = x[i]
#         elif x[i] > m2:
#             m2 = x[i]
#     return m1,m2
# if __name__ == '__main__':
#     print(get_max2([4,3,1,2,5]))

# ex5:计算指定的年月日是这一年的第几天

# def is_leap_year(year):
#     """
#     判断指定的年份是不是闰年

#     :param year: 年份
#     :return: 闰年返回True平年返回False
#     """
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# def which_day(year, month, date):
#     """
#     计算传入的日期是这一年的第几天

#     :param year: 年
#     :param month: 月
#     :param date: 日
#     :return: 第几天
#     """
#     days_of_month = [
#         [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
#         [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     ][is_leap_year(year)]
#     total = 0
#     for index in range(month - 1):
#         total += days_of_month[index]
#     return total + date


# def main():
#     print(which_day(1980, 11, 28))
#     print(which_day(1981, 12, 31))
#     print(which_day(2018, 1, 1))
#     print(which_day(2016, 3, 1))


# if __name__ == '__main__':
#     main()

# # ex6: 打印杨辉三角
# def main():
#     num = int(input('Number of rows: '))
#     yh = [[]] * num
#     # print(yh)
#     for row in range(len(yh)):
#         yh[row] = [None] * (row + 1)
#         # print(yh[row])
#         for col in range(len(yh[row])):
#             if col == 0 or col == row:
#                 yh[row][col] = 1
#             else:
#                 yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
#             print(yh[row][col], end='\t')
#         print()

# if __name__ == '__main__':
#     main()

# # case1:双色球选号--todo
# from random import randrange, randint, sample


# def display(balls):
#     """
#     输出列表中的双色球号码
#     """
#     for index, ball in enumerate(balls):
#         if index == len(balls) - 1:
#             print('|', end=' ')
#         print('%02d' % ball, end=' ')
#     print()


# def random_select():
#     """
#     随机选择一组号码
#     """
#     red_balls = [x for x in range(1, 34)]
#     selected_balls = []
#     selected_balls = sample(red_balls, 6)
#     selected_balls.sort()
#     selected_balls.append(randint(1, 16))
#     return selected_balls


# def main():
#     n = int(input('机选几注: '))
#     for _ in range(n):
#         display(random_select())


# if __name__ == '__main__':
#     main()

# # case2:约瑟夫环问题--todo
# """
# 《幸运的基督徒》
# 有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
# """


# def main():
#     persons = [True] * 30
#     counter, index, number = 0, 0, 0
#     while counter < 15:
#         if persons[index]:
#             number += 1
#             if number == 9:
#                 persons[index] = False
#                 counter += 1
#                 number = 0
#         index += 1
#         index %= 30
#     for person in persons:
#         print('基' if person else '非', end='')


# if __name__ == '__main__':
#     main()

# # case3:井字棋游戏
# import os


# def print_board(board):
#     print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
#     print('-+-+-')
#     print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
#     print('-+-+-')
#     print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


# def main():
#     init_board = {
#         'TL': ' ', 'TM': ' ', 'TR': ' ',
#         'ML': ' ', 'MM': ' ', 'MR': ' ',
#         'BL': ' ', 'BM': ' ', 'BR': ' '
#     }
#     begin = True
#     while begin:
#         curr_board = init_board.copy()
#         begin = False
#         turn = 'x'
#         counter = 0
#         os.system('clear')
#         print_board(curr_board)
#         while counter < 9:
#             move = input('轮到%s走棋, 请输入位置: ' % turn)
#             if curr_board[move] == ' ':
#                 counter += 1
#                 curr_board[move] = turn
#                 if turn == 'x':
#                     turn = 'o'
#                 else:
#                     turn = 'x'
#             os.system('clear')
#             print_board(curr_board)
#         choice = input('再玩一局?(yes|no)')
#         begin = choice == 'yes'


# if __name__ == '__main__':
#     main()

"""
day08--面向对象编程基础
"""
# # class
# class Student(object):
#     # __init__是一个特殊方法用于在创建对象时进行初始化操作
#     # 通过这个方法我们可以为学生对象绑定name和age两个属性
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def study(self, course_name):
#         print('%s正在学习%s.' % (self.name, course_name))
    
#     def watch_movie(self):
#         if self.age < 18:
#             print('%s只能观看《熊出没》.' % self.name)
#         else:
#             print('%s正在观看岛国爱情大电影.' % self.name)

# def main():
#     stu1 = Student('xsy', 18)
#     stu1.study('Python程序设计')
#     stu1.watch_movie()

# if __name__ == '__main__':
#     main()

# class Test:
#     def __init__(self, foo):
#         self.__foo = foo
#     def __bar(self):
#         print(self.__foo)
#         print('__bar')

# def main():
#     test = Test('hello')
#     test.__bar()
#     print(test.__foo)

# if __name__ == '__main__':
#     main()

# # ex1:定义一个类描述数字时钟
# from time import sleep
# class Clock(object):
#     def __init__(self, hour=0, minute=0, second=0):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
    
#     def run(self):
#         self.second += 1
#         if self.second == 60:
#             self.second = 0
#             self.minute += 1
#             if self.minute == 60:
#                 self.minute = 0
#                 self.hour += 1
#                 if self.hour == 24:
#                     self.hour = 0
    
#     def show(self):
#         return '%02d:%02d:%02d' % (self.hour, self.minute, self.second)

# def main():
#     clock = Clock(23, 59, 58)
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()

# if __name__ == '__main__':
#     main()

# # ex2:定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法
# from math import sqrt
# class Point(object):
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
    
#     def move_to(self, x, y):
#         self.x = x
#         self.y = y
    
#     def move_by(self, dx, dy):
#         self.x += dx
#         self.y += dy
    
#     def distance_to(self, other):
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return sqrt(dx ** 2 + dy ** 2)
    
#     def __str__(self):
#         return '(%s, %s)' % (str(self.x), str(self.y))

# def main():
#     p1 = Point(3, 5)
#     p2 = Point()
#     print(p1)
#     print(p2)
#     p2.move_by(-1, 2)
#     print(p2)
#     print(p1.distance_to(p2))

# if __name__ == '__main__':
#     main()

"""
day09--面向对象进阶
"""
