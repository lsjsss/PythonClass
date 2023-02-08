s = 'Hello World\n 文本文件的读取方法\n 文本文件的写入方法\n'


with open('sample.txt') as fp: # 默以使用cp936编码
    print(fp.read0)

print(' 字符串 s 的长度()', len(s))

with open('sample.txt') as fp: # 假设文件天书CP936编码
    for line in fp: # 文件对象可以直接送代
        print(line)

fp = open('sample.txt')
print(fp.readlines())
fp.close()