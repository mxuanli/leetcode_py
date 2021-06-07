# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        r = ListNode()
        r.next = head
        back_node = r
        while head:
            if head.val == val:
                back_node.next = head.next
                head = head.next
            else:
                back_node = head
                head = head.next
        return r.next
