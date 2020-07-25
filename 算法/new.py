def quick_sort(alist: list):
    if len(alist) <= 1:
        return alist
    first = alist[0]
    left = 0
    right = len(alist)-1
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
    return quick_sort(alist[:right]) + [first] + quick_sort(alist[right + 1:])
