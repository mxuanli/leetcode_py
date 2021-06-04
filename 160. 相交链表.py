# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        HA = headA
        HB = headB
        while HA != HB:
            if HA != None:
                HA = HA.next
            else:
                HA = headB
            if HB != None:
                HB = HB.next
            else:
                HB = headA
        return HA


class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        tmp = dict()
        while headA:
            tmp[headA] = True
            headA = headA.next
        while headB:
            if headB in tmp:
                return headB
            headB = headB.next
        return None


c = ListNode(8)
d = ListNode(4)
e = ListNode(5)

headA = ListNode(4)
a2 = ListNode(1)
headA.next = a2
headA.next.next = c
headA.next.next.next = d
headA.next.next.next.next = 3

b2 = ListNode(6)
b3 = ListNode(1)
headB = ListNode(5)
headB.next = b2
headB.next.next = b3
headB.next.next.next = c
headB.next.next.next.next = d
headB.next.next.next.next = e

s = Solution()
r = s.getIntersectionNode(headA, headB)
print(r.val)
