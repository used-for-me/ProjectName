# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def hh(ll):
            a1 = ll.val
            a0 = 1
            while ll.next:
                ll = ll.next
                a1 += ll.val * (10 ** a0)
                a0 += 1
            return a1

        ss = hh(l1) + hh(l2)
        f = ListNode(ss % 10)
        ss = int(ss / 10)
        aa = f
        while ss > 0:
            s = ListNode(ss % 10)
            aa.next = s
            aa = s
            ss = int(ss / 10)
        return f

# # ss = 'end'.join('123456')
# # ss = ss.split('end')
# # print(ss)
# a1 = [2, 4, 3]
# a2 = [5, 6, 4]
#
#
# def jj(ss):
#     f = ListNode(int(ss[len(ss) - 1]))
#     print(f.val)
#     aa = f
#     for i in tuple(reversed(range(0, len(ss) - 1))):
#         s = ListNode(int(ss[i]))
#         print(s.val)
#         s.next = None
#         aa.next = s
#         aa = s
#     return f


# def hh(ll):
#     a1ss = ''
#     a1ss += str(ll.val)
#     while ll.next:
#         ll = ll.next
#         a1ss = str(ll.val) + a1ss
#     a1ss = int(a1ss)
#     return a1ss
#
#
# print(hh(jj(a1)))
# print(hh(jj(a2)))
