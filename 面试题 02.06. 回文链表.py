# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:

    def isPalindrome(self, head: ListNode) -> bool:
        node_list = list()
        while head:
            node_list.append(head.val)
            head = head.next
        return node_list == node_list[::-1]
