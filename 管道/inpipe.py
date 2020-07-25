import sys

print('this is inpipe module')

with open('hh.txt', 'w') as fp:
    for i in sys.argv:
        fp.write('kk')

ss = []
# 取管道内的数据
for i in sys.stdin:
    if i is not None and i != ' ':
        ss.append(i)
print(ss)
