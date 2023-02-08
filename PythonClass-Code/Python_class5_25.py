src = open('test.txt', 'w')
src.write('nihao\nhelloworld')

print(src.tell())  # 返回文件指针的当前位置
print(src.readable())  # 测试当前文件是否可读
print(src.writable())  # 测试当前文件是否可写

src.flush()  # 把缓冲区的内容写入文件，但不关闭文件
src.close()

with open('f:\\testpythonfile\\test.txt', 'r') as src, open('test_new.txt', 'w') as dst:
    dst.write(src.read())

fp = open('f:\\testpythonfile\\test.txt')
print(fp.read())

print('*' * 20)
fp.seek(2)
print(fp.readline())

print('-' * 20)
fp.seek(0)
print(fp.readlines())
