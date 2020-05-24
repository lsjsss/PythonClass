# 例7-5  读取文本文件data.txt（文件中每行存放一个整数）中所有整数，
# 将其按升序排序后再写入文本文件data_asc.txt中。

with open('f:\\testpythonfile\\data.txt', 'r') as fp:
    data = fp.readlines()
data = [int(line.strip()) for line in data]
data.sort()
data = [str(i) + '\n' for i in data]
with open('f:\\testpythonfile\\data_asc.txt', 'w') as fp:
    fp.writelines(data)
