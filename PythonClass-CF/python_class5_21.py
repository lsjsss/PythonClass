s = '500\n123456\n5555555\n1\n'

with open('f:\\sample.txt', 'w') as fp:
    fp.write(s)
#
# with open('f:\\sample.txt') as fp:
#     print(fp.read())

# f = open('f:\\sample.txt', 'r')
# s = f.read(5)  # 读取文件的前 5 个字符
# f.close()
# print('s=', s)
# print('字符串 s 的长度(字符个数)=', len(s))


# with open('f:\\sample.txt')as fp:  # 井假设文件采用CP936编码
#     for line in fp:  # 并文件对象可以直接迭代
#         print(line)


# s='中国山东烟台SDIBT'
# fp = open(r'f:\\sample.txt', 'w')
# fp.write(s)
#
# 关闭文件流
# fp.close()
# fp = open(r'f:\\sample.txt', 'r')
# 读取前 3 个字符
# print(fp.read(3))
# fp.seek(2)
# print(fp.read(1))
# fp.seek(13)
# print(fp.read(1))
# fp.seek(3)
# print(fp.read(1))


# # 读取文件
# with open('f:\\sample.txt', 'r') as fp:
#     # 文件对象，读取所有行(直到结束符 EOF)并返回列表，对所有内容进行排序
#     data = fp.readlines()
# # 移除字符串头尾指定的字符（默认为空格）或字符序列，删除两端空白字符，强制转换为整型
# data = [int(line.strip()) for line in data]
# # 对原列表进行排序
# data.sort()
# data = [str(i) + '\n' for i in data]
# with open('f:\\sample.txt', 'w') as fp:
#     # 向文件中写入一序列的字符串
#     fp.writelines(data)


with open('f:\\sample.txt', 'r')as fp:
    data = fp.readlines()
data = [line.strip() for line in data]
data = ','.join(data)
data = data.split(',')
data = [int(item) for item in data]
data.sort()
data = ','.join(map(str, data))
with open('f:\\sample.txt', 'w') as fp:
    fp.write(data)
