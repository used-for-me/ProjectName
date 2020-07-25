import random
from copy import deepcopy, copy


def heap_adjust(alist: list, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and alist[child] < alist[child + 1]:
            child += 1
        if alist[child] > alist[root]:
            alist[root], alist[child] = alist[child], alist[root]
            root = child
        else:
            break


def heap_sort(alist: list):
    first = len(alist) // 2 - 1
    for start in range(first, -1, -1):
        heap_adjust(alist, start, len(alist) - 1)

    for end in range(len(alist) - 1, 0, -1):
        alist[0], alist[end] = alist[end], alist[0]
        heap_adjust(alist, 0, end - 1)


if __name__ == '__main__':
    xlist = [random.randint(1, 1000) for i in range(1000)]
    print(xlist)
    a = list(deepcopy(xlist))
    a.sort()
    print("a:", a)
    heap_sort(xlist)
    myflag = True
    for i, j in zip(a, xlist):
        if i != j:
            myflag = False
            break
    print("是否一致", myflag)

    print("排序后：", xlist)
    flag = 0
    ok = True
    for i in xlist:
        if i < flag:
            ok = False
            break
        else:
            flag = i
    print("顺序", ok)
