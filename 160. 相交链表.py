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
