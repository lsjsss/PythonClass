import time


def caculate_time(f):
    def inner(*args, **kwargs):
        print('*' * 10)
        # start_time = time.time()
        ret = f(*args, **kwargs)
        # time.sleep(1)
        # end_time = time.time()
        # print("函数运行时间：", ret)

        # print('*' * 10)
        return ret

    return inner


@caculate_time
def add(m, n):
    return m + n


print(add(1, 2))

print(11111111111111)
x = 2 + 9 * ((3 * 12) - 8) // 10

# a = 10
# b = 20
# print(a and b)

a, b, c, d = 1, 3, 5, 4
if a < b:
    if c < d:
        x = 1
    elif a < c:
        if b < d:
            x = 2
        else:
            x = 3
    else:
        x = 6
else:
    x = 7

sc = 'abcdefg'
print(sc[::-1])

s1 = [1, 2, 3, 4]

s2 = [5, 6, 7]

print(len(s1 + s2))

for i in range(1, 6):

    if i % 4 == 0:

        break

    else:

        print(i, end=",")



sum=0

for i in range(100):

    if(i%10):

        continue

    sum = sum + i

print(sum)

g = lambda x, y=3, z=5: x*y*z
print(g(1))
