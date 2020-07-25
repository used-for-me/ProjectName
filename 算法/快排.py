import random
from timeit import repeat


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


def start():
    xlist = [random.randint(1, 1000) for i in range(7)]
    # print(repeat('quick_sort(xlist)', 'from __main__ import quick_sort',
    #              globals={"xlist": xlist}, number=1000, repeat=6))
    x = quick_sort(xlist)
    print("排序：", x)
    # flag = 0
    # ok = True
    # for i in x:
    #     if i < flag:
    #         ok = False
    #         break
    #     else:
    #         flag = i
    # print("顺序", ok)


if __name__ == '__main__':
    start()
