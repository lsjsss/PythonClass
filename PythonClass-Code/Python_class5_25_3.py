fp = open('data.txt','w')
for i in [ '1','3','333','9','12']:
    fp.write(i +'\n')
fp. close()

with open( 'data.txt' 'r') as fp:
    data = fp.readlines()

data = [int(line.strip()) for line in data]
data.sort()
data = [str(i) + '\n' for i in data]

