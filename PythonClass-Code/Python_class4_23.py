# 输出杨辉三角形
def triangle():
    N = [1]
    while True:
        yield N  # generator特点在于：在执行过程中，遇到yield就中断，下次又继续执行
        N.append(0)  # 每次都要在最后一位加个0，用于后续的叠加
        N = [N[i] + N[i - 1] for i in range(len(N))]

def print_triangle(x):
    a = 0
    for t in triangle():  # 这里可以每次调用一个N（得力于Yield函数）
        print(t)
        a += 1
        if a == x:
            break

print_triangle(10)  # 打印10行



N = [1]
for i in range(10):
    print(N)
    N.append(0)
    N = [N[k] + N[k - 1] for k in range(i + 2)]
