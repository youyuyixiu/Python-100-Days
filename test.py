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
