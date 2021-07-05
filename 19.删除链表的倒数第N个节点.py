# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        len_linked = 0
        node = head
        # 算长度
        while node:
            len_linked += 1
            node = node.next
        # 算位置
        del_node = len_linked - n
        if del_node == 0:
            return head.next
        # 删节点
        node = head
        for i in range(1, del_node):
            node = node.next
        node.next = node.next.next
        return head


class Solution1:
    # 双指针
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = ListNode()
        node.next = head
        fast = head
        slow = node
        for i in range(n):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return node.next


class Solution3:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
