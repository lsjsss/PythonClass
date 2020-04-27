class car():
    # 类属性
    price = 100000

    #对象属性,首先调用此函数
    def __init__(self):
        self.height = 50
        self.width = 60

    # 实例方法
    def yundong(self):
        print('我会跑')

    def __str__(self):
        return f'String,我的高度是{self.height}\n'


# 实例化对象
car1 = car()
print(car1, car)

# 调用属性
print(car1.price)

# 调用函数
car1.yundong()

car.pinpai = 'benchi'
print(car1.pinpai)

# 增加对象属性
car1.color = 'red'

print(car1.width)
car1.height = 50
print(car1.height)

import types

def shache(self):
    print('shache')

car1.shache = types.MethodType(shache, car1)
car1.shache()




