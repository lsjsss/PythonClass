# 例7-6  编写程序，保存为demo6.py，运行后生成文件demo6_new.py，
# 其中的内容与demo6.py一致，但是在每行的行尾加上了行号。

filename = 'f:\\testpythonfile\\demo6.py'
with open(filename, 'r') as fp:
    lines = fp.readlines()
# 假设每行最长不超过100个字符，在第100列插入行号
lines = [line.rstrip() + ' ' * (100 - len(line)) + '#' + str(index) + '\n' for index, line in enumerate(lines)]
with open(filename[:-3] + '_new.py', 'w') as fp:
    fp.writelines(lines)
