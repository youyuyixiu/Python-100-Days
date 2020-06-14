"""
使用变量保存数据并进行算术运算
"""
a = 321
b = 123
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

"""
使用type()检查变量的类型
"""
a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'complex'>
print(type(d)) # <class 'str'>
print(type(e)) # <class 'bool'>

# print(ord("a"))
# print(chr(65))

"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串
"""
# a = int(input('a = '))
# b = int(input('b = '))
# print('%d + %d = %d' % (a, b, a + b))
# print('%d - %d = %d' % (a, b, a - b))
# print('%d * %d = %d' % (a, b, a * b))
# print('%d / %d = %f' % (a, b, a / b))
# print('%d // %d = %d' % (a, b, a // b))
# print('%d %% %d = %d' % (a, b, a % b))
# print('%d ** %d = %d' % (a, b, a ** b))

"""
赋值运算符和复合赋值运算符
"""
a = 10
b = 3
a += b # 相当于：a = a + b
a *= a + 2 # 相当于：a = a * (a + 2)
print(a) # 想想这里会输出什么

"""
比较、逻辑和算身份运算符的使用
"""
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0) # flag0 = True
print('flag1 =', flag1) # flag1 = True
print('flag2 =', flag2) # flag2 = False
print('flag3 =', flag3) # flag3 = False
print('flag4 =', flag4) # flag4 = True
print('flag5 =', flag5) # flag5 = False
print(flag1 is True) # True
print(flag2 is not False) # False

"""
ex1 将华氏温度转换为摄氏温度
"""
# f = float(input('华氏温度='))
# c = (f - 32) / 1.8
# print('%.1f华氏温度 = %.1f摄氏温度' % (f, c))

"""
ex2 输入半径计算圆的周长和面积
"""
# import math

# radius = float(input('请输入圆的半径：'))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius * radius
# print('圆的周长是：%.2f' % perimeter)
# print('圆的面积是：%.2f' % area)

"""
ex3 输入年份判断是不是闰年
"""
year = int(input('请输入年份：'))
is_leap_year =  (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(is_leap_year)
