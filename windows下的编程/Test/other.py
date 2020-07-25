class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        def sort(alist, flag):
            flag = flag
            a = alist[0:flag + 1]
            b = list(reversed(alist[flag + 1:]))
            a1 = a.pop()
            b1 = b.pop()
            for k in range(len(alist)):
                if a1 <= b1:
                    alist[k] = a1
                    if a:
                        a1 = a.pop()
                    else:
                        a1 = float('inf')
                else:
                    alist[k] = b1
                    if b:
                        b1 = b.pop()
                    else:
                        b1 = float('inf')
            return alist

        for i in range(len(A)):
            if A[0] >= 0:
                for j in range(len(A)):
                    A[j] *= A[j]
                return A

            if A[len(A) - 1] < 0:
                for j in range(len(A)):
                    A[j] *= A[j]
                return reversed(A)

            if A[i] < 0 <= A[i + 1]:
                for j in range(len(A)):
                    A[j] *= A[j]
                return sort(A, i)


f = Solution()
ss = f.sortedSquares([0, 5])
print(ss)

