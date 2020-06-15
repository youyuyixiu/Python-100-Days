"""
用户身份验证
"""
# username = input('请输入用户名: ')
# password = input('请输入口令: ')
# # 用户名是admin且密码是123456则身份验证成功否则身份验证失败
# if username == 'admin' and password == '123456':
#     print('身份验证成功!')
# else:
#     print('身份验证失败!')

"""
分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
能使用扁平化的结构时就不要使用嵌套
"""
# x = float(input('x = '))
# if x > 1:
#     y = 3 * x - 5
# elif x >= -1:
#     y = x + 2
# else:
#     y = 5 * x + 3
# print('f(%.2f) = %.2f' % (x, y))

"""
ex1 英制单位英寸和公制单位厘米互换
"""
# value = float(input('请输入长度：'))
# unit = input('请输入单位：')
# if unit == 'in' or unit == '英寸':
#     print('%.2f英寸 = %.2f厘米' % (value, value * 2.54))
# elif  unit == 'cm' or unit == '厘米':
#     print('%.2f厘米 = %.2f英寸' % (value, value / 2.54))
# else:
#     print('输入有误，请重新输入：')

"""
ex2 百分制成绩转换为等级制成绩
"""
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
# print(grade)

"""
ex3 判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积
"""
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长：%.2f' % (a + b + c))
    p = (a + b + c) / 2
    area = p * (p - a) * (p - b) * (p - c)
    print('面积：%.2f' % (area))
else:
    print('无法构成三角形')