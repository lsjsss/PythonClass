# import turtle
#
# spiral =  turtle.Turtle()
#
# for i in range(20):
#     spiral.forward(i * 10)
#     spiral.right(144)
#
# turtle.done()
#
# import random
# number = random.random(1, 10)
#
# list = []
# for i in range(1, 10):
#     list.append(random.randint(1, 10))
# print(list)
#
# int_a=10
# int_b=0b10
# int_c=0o10
# int_d=0x10
#
# print(int_a)
# print(int_b)
# print(int_c)
# print(int_d)

# age = int(input("please input your age:"))
# if age >= 18:
#     print("已成年！")
# else:
#     print("未成年！")


# for i in [0, 1, 2]:
#     print(i)
#
# sum=0
# for i in range(1,101):
#     sum+=i
# print("1~100的累加值是：%d"%sum)
#
# while True:
#     sum+=1
#     print(sum)


# a = input(123)
# if a == 1:
#     pass
# else:
#     pass
# for i in range(1,101):
#     if i%3==0 and i%5==0 and i%7==0:
#         print("同时能够被3，5，7整除的最小数是%d"%i)
#         break
# else:
#     print("未找到能够被3，5，7整除的数！")

# sum=0
# for i in range(100):
#     if(i%10):
#         continue
#     print(i)
#     sum=sum+i
# print(4%4)


# print("我爱python") #单个字符串的输出
# print("我爱python"*5) #5个重复字符串的输出
# print("中国，"+"你好！") #多个字符串输出，用加号连接
# print("中国，","你好！") #多个字符串输出，用逗号连接
# print('''中国，
# 你好！''') #带换行的输出
# print("姓名：",end=" ")
# print("学号") #输出不换行
#
#
# str1="abcdef"
# for i in range(-6,6):
#     print(str(i),str1[i])
#

# name="abcdef"
# print(name[0:3])     # 取下标 0~2 的字符
# print(name[2:])     # 取下标从 2 开始到最后的字符
# print(name[:2])     # 取下标从 0 开始到 1 的字符
# print(name[:])     # 取字符串所有的值
# print(name[::2])    # 从头到尾，取步长为 2 对应的字符
# print(name[1:-1])    # 取下标从 1 开始到倒数第二字符
# print(name[0:6:3])    # 取下标从 0~5 并且步长为 3 对应的字符



# str1="abcdabcdabcd"
# str2="1"
# str1.replace()



# list=[87,69,75,93]
# j=0
# while j<len(list):
#     print("list列表中的第%d个元素的值是：%d"%((j+1),list[j]))
#     j+=1
#
# list=[87,69,75,93]
# for i in list:
#     print(i)
#
#
# for index in range(len(list)):
#     print("list列表中索引为%d的元素的值是：%d"%((index),list[index]))





# list1=["李杨","刘文","张兵","丁鑫"]
# list2=[87,69,75,93]
# for i,j in zip(list1,list2):
#     print("%s%d"%(i,j))

# list=[74,75,87,62,95,57,84]
# print("原列表：",list)
# list.sort()     #sort函数默认空为升序排列
# print("升序排序",list)
# list.sort(reverse=True)     #sort函数的reverse指定True时，列表为降序排列
# print("降序排序",list)



# list=[74,75,87,62,95,57,84]
# print("原列表：",list)
# list.reverse()
# print("使用reverse()函数进行反向排序",list)
# print("使用切片进行反向排序",list[::-1])
#
#
#
# list=[[74,75,87,62,95,57,84],[87,62,95,57,84],[62,95,57,84]]
# print(list) # 输出整个列表
# print(list[0]) # 输出列表第一组元素
# print(list[0][0]) # 输出列表第一组第一个元素
# print(list[1][0:4]) # 输出列表第二组第1到4个元素
#
# list=[[74,75,87,62,95,57,84],[87,62,95,57,84],[62,95,57,84]]
# index=0     #使用索引遍历被嵌套列表的元素
# for i in list:
#     for j in list[index]:
#         print(j,end=" ")
#     index+=1
#     print()


# s1=[1,2,3,4]
# s2=[5,6,7]
# print([1,2,3]*3)
#
# tuple1=()
# print(tuple1)
# tuple2=("1",2,3)
# print(tuple2)
# tuple3=(4,5,6)
# print(tuple3)


# tuple=(1,2,3,4,5,6)
# print(tuple[0])

# print(type((1,2,3,4)))
# print(tuple([1,2,3]))


# dict={"a":"1","b":"2","c":"3"}
# dict["d"]="4" # 增
# dict["b"]="5" # 删
# del dict["c"] # 改
# print(dict["a"]) # 查

# s = "abc"
# print(s[0 : len(s)-1])

from datetime import datetime
# dt = datetime.now()
# print( '时间：(%Y-%m-%d %H:%M:%S %f): ' , dt.strftime( '%Y-%m-%d %H:%M:%S' ))

# from datetime import datetime
# print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# from datetime import datetime
# print('今天是本年中的第%s天，第%s周的%s' %(datetime.now().strftime('%j'), datetime.now().strftime('%U'), datetime.now().strftime( '%A' ) ))


# from datetime import datetime
# # print('%s %s %s' %(datetime.now().strftime( '%a' ), datetime.now().strftime( '%b' ), datetime.now().strftime( '%d' ), datetime.now()))
# print(datetime.now().strftime('%b %a %d %H:%M:%S %Y'))


# def num(i):
#     if (i == 1):
#         return i
#     else:
#         return i * num(i-1)
# print(num(5))


# print('今天是今年的第%s天 '  % datetime.now().strftime( '%j' ) )
# print('今周是今年的第%s周 '  % datetime.now().strftime( '%U' ) )


# print("%s" %dict.items())

# dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}
#
# print("字典值 : %s" % dict.items())
#
# # 遍历字典列表
# for key, values in dict.items():
#     print (key, values)



# dict1={"姓名":"李天","性别":"男","年龄":29}
# #keys方法的使用
# print(dict1.keys())
# list1=list(dict1.keys())
# print(list1)
#
# #values方法的使用
# print(dict1.values())
# list2=list(dict1.values())
# print(list2)
#
# #items方法的使用
# print(dict1.items())
# list3=list(dict1.items())
# print(list3)
#
# #setdefault方法的使用
# dict1.setdefault("学号",201865112503)
# print(dict1)
# print(dict1.setdefault("学号",201865112530))
# print(dict1)
#
# #update方法的使用
# dict2={"姓名":"李天","学号":201865112503}
# dict3={"姓名":"张琴"}
# dict1.update(dict2)
# print("1:",dict1)
# dict1.update(dict3)
# print("2:",dict1)
#
# #fromkeys 方法的使用
# dict4={}
# seq={"方便面","火腿肠","饼干"}
# dict4=dict.fromkeys(seq)
# print("1:",dict4)
# dict4=dict.fromkeys(seq,0)
# print("2:",dict4)
#
# #copy方法的使用
# dict5=dict3.copy()
# print(dict5)
# print(id(dict3),id(dict5))
#
#
# def test(a, b):
#     print("a=", a, "b=", b)
#
#
# test(1, 3)
# test(5 + 6, 8)
#
#
# test(a=1,b=3)
# test(b=3,a=1)
# test(2,b=4)
#
# print('--------------------------')
# def test1(a=1,b=1):
#     print("a=",a,"b=",b)
# test1()
# test1(5)
# test1(1,2)
# test1(b=2,a=5)
# test1()
# test1(3,b=5)
#
#
# def student(name, *other):  # other 参数是不定长参数，接收的数据保存为元组
#     print(name, end=":")
#     print(other)
# student("李天", "男", 19, 172.5)
# student("李天", 172.5)
#
#
# def student(name,**other):
#     print(name,other)
# student("李天",sex="男",age=18)
# student(sex="男",age=18,name="李天")
#
#
#
#
# def student(name,*course,**other):
#     print(name,course,other)
# student("李天","英语","Python",sex="男",age=18)
#
#
#
#
# def function1():         # 函数function1的定义
#     print("我是函数1！")
# def function2():         # 函数function2的定义
#     print("我是函数2！")
#     function1()         # 在 function2 函数中调用 function1 函数
# function2()          #调用 function2 函数
#
#
# def func5(a,b,*c):
#         print(a,b)
# func5(1,2,3,4,5,6)
#
#
#
# g = lambda x,y=3,z=5:x*y*z
# print(g(1))


# add = lambda x, y: x + y
# print(add(2, 3))



# for i in range(1 ,3):
#     for j in range(2, 5):
#         print(i*j)

# for s in "testatest":
#     if s=="a" or s=="e":
#         continue
#     print(s, end='')


# list_one=[4,5,6]
# list_two=list_one
# list_one[2]=3
# print(list_two)
#
a = 9
b = 2
# print(a + b)
# print(a // b)
# print(a % b)
# print(a ** b)

print(eval('2+4/5'))

print(16/4-2**5*8/4%5//2)
print(3*4**2//8%7)

def Sum(a, b=3, c=5):
    print(a,b,c)
Sum(8,2)

print(3>2>1)


list_demo=[1,2,3,4,5,'a','b']
print(list_demo[1],list_demo[5])


s=['a','b']
s.append([1,2])
s.insert(1,7);
print(s)


print( 0.1 + 0.2 == 0.3 )

a = b = 2


# x=input()
# print(x)

a=1
b=2
print(a,b)



print(list(map(str, [1, 2, 3])))

x=3
x+=6
print(x)


aList = [3, 4, 5, 6, 7, 9, 11, 13, 15, 17]
print(aList[3:7])


print(int(4**0.5))
print(1<2<3)

print(sum(range(1, 10)))
print('The first:{1}, the second is {0}'.format(65, 97))


print('-----------------')

print(sorted([111,2,33], key=lambda x:len(str(x))))
for i in range(3):
        print(i, end=',')

y = {1:2,2:3,3:4}
print(sum(y))

print(3 |5)

# x=3
# x+=6
# print(0 or 5)

x={i:str(i+3) for i in range(3)}
print("".join(x.values()))

