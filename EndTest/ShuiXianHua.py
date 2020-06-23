# 1、任务内容:
# 水仙花数是一个三位整数，如153是一个水仙花数，是因为该数
# 的百位的立方、十位的立方、个位的立方成之和等于该数本身，如下所
# 示:
# 13+53+33=153
# ●程序编写要求:
# ●使用for语句完成;统计水仙花数个数的值请保存到变量
# 中，并要求自动进行统计
# 。输出结果如下图所示:
# 所有三位效中的水仙花数如下所示:
# 153
# 370
# 371
# 407
# 共有4个!
# 2、任务提交要求:
# .提交程序的代码及运行结果的截图
# 。要求程序的第一 行为注释，内容是:小组名+姓名，如:
# 第1组某某某

import math

print("所有三位数中的水仙花数如下所示:")
for i in range(100, 1000):
    a = int(i % 10)
    b = int((i / 10) % 10)
    c = int(i / 100)
    if math.pow(a, 3) + math.pow(b, 3) + math.pow(c, 3) == i:
        print(i)