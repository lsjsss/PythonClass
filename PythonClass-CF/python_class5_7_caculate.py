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




