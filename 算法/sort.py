import random
from copy import deepcopy


def quick_sort(alist: list):
    if len(alist) <= 1:
        return alist
    left = 0
    right = len(alist) - 1
    first = alist[0]
    while left < right:
        while left < right:
            if alist[right] < first:
                alist[left] = alist[right]
                break
            else:
                right -= 1
        while left < right:
            left += 1
            if alist[left] > first:
                alist[right] = alist[left]
                right -= 1
                break

    return quick_sort(alist[:left]) + [first] + quick_sort(alist[left + 1:])


if __name__ == '__main__':
    xlist = [random.randint(1, 1000) for i in range(10000)]
    # print(repeat('quick_sort(xlist)', 'from __main__ import quick_sort',
    #              globals={"xlist": xlist}, number=1000, repeat=6))
    a = list(deepcopy(xlist))
    a.sort()
    x = quick_sort(xlist)
    print("排序：", x)

    print("a:", a)
    myflag = True
    for i, j in zip(a, x):
        if i != j:
            myflag = False
            break
    print("是否一致", myflag)

