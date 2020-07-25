# 无穷大

INF = float('inf')

a, b, c, d, e, f, g, h = range(8)
a_list = [
    [0, 4, 6, 6, INF, INF, INF],     # 0
    [-4, 0, 1, INF, 7, INF, INF],    # 1
    [-6, -1, 0, -2, 6, 4, INF],      # 2
    [-6, INF, 2, 0, INF, 5, INF],    # 3
    [INF, -7, -6, INF, 0, -1, 6],    # 4
    [INF, INF, -4, -5, 1, 0, 8],     # 5
    [INF, INF, INF, INF, -6, -8, 0]  # 6
]
print(a_list[a][g] is INF)

