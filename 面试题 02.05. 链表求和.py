# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 和第二题一样


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode(0)
        tmp = head
        while l1 or l2 or carry:
            if l1:
                num1 = l1.val
                l1 = l1.next
            else:
                num1 = 0
            if l2:
                num2 = l2.val
                l2 = l2.next
            else:
                num2 = 0
            add = num1 + num2 + carry
            if add >= 10:
                carry = add // 10
                add = add % 10
            else:
                carry = 0
            head.next = ListNode(add)
            head = head.next
        return tmp.next
