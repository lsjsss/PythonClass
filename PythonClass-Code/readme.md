### 数学运算
> abs 求数值的绝对值
```python
abs(2)
```

> 返回两个数值的商余数
```pyton
divmod(10,3)
```

> 返回迭代对象的元素中最大值或者所有参数的最大值
```pyton
max(-1,1,2,3,4)
max("1234567")
max(-1,0,key=abs)
```

> 返回可迭代对象的元素中的最小值或者所有参数的最小值
```pyton
min(-1,1,2,3,4)
min("1234567")
min(-1,0,key=abs)
```

> 两个值取幂运算值，或与其他
```pyton
pow(2,3)
pow(2,3,5)  #(2,3)/5
pow(2,3,4)
pow(2,3,4)
```

> 对浮点数进行四舍五入求值
```pyton
round(1.45677888)
round(1.4567787888,2)
```

> 对元素类型时数值可迭代对象中的每个元素求和
```pyton
sum((1,2,3,4))
sum([1,2,3,4])
sum((1.1,1.2,1.3))
sum((1,2,3,4),-10)
sum((1,2,3,4),3)
```

### 类型转换
> 根据传入的参数的逻辑值创建一个新的布尔值
```pyton
bool()
bool(1)
```

> 根据传入的参数创建一个新的整数
```pyton
int()
int(3)
int(3, 6)
```

> 根据传入的参数创建一个新的浮点数
```pyton
float()
float(3)
float('3')
```
> 根据传入参数创建一个性的复数
```pyton
complex()
complex('1+2j')
complex(1, 2)
```

> 返回一个对象的字符串表现形式(给用户)
```pyton
str()
str(None)
str('abc')
str(123)
```

> 根据传入的参数创建一个新的元组
```pyton
tuple()
tuple('121')
```

> 根据传入的参数创建一个新的列表
```pyton
list()
list['a', 'b', 'c', 'd']
```

> 根据传入的参数创建一个新的字典
```pyton
dict()
dict(a4=1, b4=2)
dict(zip(['a', 'b'], [1, 2]))
dict(((('a', 1)('b', 2))))
```

> 根据传入的参数创建一个新的集合
```pyton
set()
a5 = set(range(10))  ##传入可迭代对象，创建集合
```

> 根据传入的参数创建一个新的不可变集合
```pyton
a5 = frozenset(range(10))
```

### 变量操作


### 交互操作

### 文件操作




```python
a1 = lambda x, y: x * y
print(a1(2,3))

a2 = list(range(0,100))
print(a2)

print(list(reversed(a2)))
```