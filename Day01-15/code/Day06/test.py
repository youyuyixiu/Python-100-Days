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
def factorial(num):
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

m = int(input('m= '))
n = int(input('n= '))
print(factorial(m) // factorial(n) // factorial(m-n))

