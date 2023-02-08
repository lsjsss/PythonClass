# 例7-13  计算文本文件中最长行的长度。
# 方法一：
f = open('f:\\testpythonfile\\test.txt','r')
allLineLens = [len(line.strip()) for line in f]
f.close()
longest = max(allLineLens)
print(longest)

# 方法二：
f = open('f:\\testpythonfile\\test.txt','r')
longest = max(len(line.strip()) for line in f)
f.close()
print(longest)