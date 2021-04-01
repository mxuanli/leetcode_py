# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        tmp = list()
        while head:
            tmp.append(head.val)
            head = head.next
        return tmp[0 - k]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2:
    def kthToLast(self, head: ListNode, k: int) -> int:
        n1, n2 = head, head
        for i in range(k):
            n2 = n2.next
        while n2:
            n1 = n1.next
            n2 = n2.next
        return n1.val
