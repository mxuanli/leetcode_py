# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def partition(self, head: ListNode, x: int) -> ListNode:
        tmp = ListNode(0)
        small = tmp
        big_head = ListNode(0)
        big = big_head
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        big = None
        small.next = big_head.next
        return tmp.next
