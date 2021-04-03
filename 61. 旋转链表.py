# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        tmp = head
        n = 1
        while tmp.next:
            tmp = tmp.next
            n += 1
        tmp.next = head
        k %= n
        for i in range(n - 1 - k):
            head = head.next
        new_head = head.next
        head.next = None
        return new_head
