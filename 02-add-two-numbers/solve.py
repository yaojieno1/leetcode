# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getVal(self, l):
        if l != None:
            return l.val
        return 0

    def getNext(self, l):
        if l != None:
            return l.next
        return None

    def addTwoNumbers(self, l1, l2):
        extra = 0
        rlt = ListNode(-1)
        ptr = rlt
        while (l1 != None or l2 != None or extra != 0):
            val   = extra + self.getVal(l1) + self.getVal(l2)
            tmp   = ListNode(val % 10)
            extra = val / 10
            if ptr.val == -1:
                rlt = tmp
                ptr = rlt
            else:
                ptr.next = tmp
                ptr = tmp
            l1 = self.getNext(l1)
            l2 = self.getNext(l2)
        return rlt
