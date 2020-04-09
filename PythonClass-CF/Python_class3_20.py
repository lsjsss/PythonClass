# import math
#
# print(math.sin(1))

number1 = [0, 1, 2, 3, 4, 5, 6, 7]
print(number1[0:3])  # 取下标0~2的字符
print(number1[2:])  # 取下标从2开始到最后的字符
print(number1[:2])  # 取下标从0开始到1的字符
print(number1[:])   # 取字符串所有的值
print(number1[::2])  # 从头到尾，取步长为2对应的字符
print(number1[1:-1])  # 取下标从1开始到倒数第二个（下标为 -1）字符
print(number1[0:6:3])  # 取下标从0~5并且步长为3对应的字符

# a = tuple(range(1, 16))
# print(a)
#
# b = {'we': 2, 'ppp': 3}
# type(a)
# d = dict(e=1, f=2, g=3)
