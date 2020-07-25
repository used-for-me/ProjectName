# 平均分组算法


n = 25
a_list = []
if n % 8 == 0:
    for i in range(0, n // 8):
        for j in range(0, 8):
            a_list.append(i + 1)
else:
    count = n // 8 + 1
    r = n // count
    low = n - count * r
    for i in range(count):
        if low > 0:
            # 每组人数
            print(r+1, end='')
            for k in range(0, r + 1):
                a_list.append(i + 1)
        else:
            # 每组人数
            print(r, end='')
            for l in range(0, r):
                a_list.append(i+1)
        low -= 1

# print(a_list)