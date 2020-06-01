import numpy as np

a = np.array([[1, 2, 3], [3, 4, 5]])
# 维度
print(a.ndim)
# 大小(形状)
print(a.shape)
# 占用大小
print(a.itemsize)

x = np.array([0, 1, 2, 3])
print(x)

x = np.array((4, 5, 6, 7))
print(x)

x = np.array([[1, 2], [9, 8], (0.1, 0.2)])
print(x)

# np.array((1, 2, 3, 4, 5))  # 把Python列表转换成数组(可以是列表或元组或二者混合:
# np.array(range(5))  # 把Python的range 对象转换成数组
# np.aray([[1, 2, 3], [4, 5, 6]])
# np.linspace(0, 10, 11)  # 生成等差数组
# np.linspace(0, 1, 11)  # 包含右端点
# np.logspace(0, 100, 10)  # 对数数组
# np.zeros((3, 3))  # 全0二维数组
# np.zeros((3, 1))  # 全0一维数组
# np.ones((3, 3))  # 全1二维数组
# np.ones((1, 3))  # 全1一维数组

