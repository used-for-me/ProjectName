import random
from timeit import repeat


def quick_sort(alist: list):
    if len(alist) <= 1:
        return alist
    first = alist[0]
    left = 0
    right = len(alist) - 1

    while left < right:
        while left < right:
            if alist[right] < first:
                break
            else:
                right -= 1
        left += 1
        while left < right:
            if alist[left] > first:
                break
            else:
                left += 1
        if left < right:
            alist[left], alist[right] = alist[right], alist[left]
            right -= 1
    alist[0], alist[right] = alist[right], alist[0]
    return quick_sort(alist[:right]) + [first] + quick_sort(alist[right + 1:])


def start():
    xlist = [random.randint(1, 1000) for i in range(1000)]
    print(repeat('quick_sort(xlist)', 'from __main__ import quick_sort',
                 globals={"xlist": xlist}, number=1000, repeat=6))
    # x = quick_sort(xlist)
    # flag = 0
    # ok = True
    # for i in x:
    #     if i < flag:
    #         ok = False
    #         break
    #     else:
    #         flag = i
    # print("顺序", ok)
    # xlist.sort()
    # print(xlist)
    # myflag = True
    # for i, j in zip(x, xlist):
    #     if i != j:
    #         myflag = False
    #         break
    # print("是否一致", myflag)


if __name__ == '__main__':
    start()
