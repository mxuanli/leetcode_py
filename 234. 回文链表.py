# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node_list = list()
        while head:
            node_list.append(head.val)
            head = head.next
        if node_list == node_list[::-1]:
            return True
        return False
