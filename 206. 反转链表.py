# Definition for singly-linked list.
"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def reverseList1(self, head: ListNode) -> ListNode:
        return self.foo(head)

    def foo(self, head: ListNode):
        if not head or not head.next:
            return head
        tmp = self.foo(head.next)  # 返回空白的头
        head.next.next = head  # 下一个值的下一个值指向当前，反转局部
        head.next = None  # 避免最后重复指向
        return tmp

    # 还是有问题
    def reverseList(self, head: ListNode) -> ListNode:
        tmp = None
        while head:
            nnl = head.next
            head.next = tmp
            tmp = head
            head = nnl
        return tmp

    def run(self):
        l1 = ListNode(1)
        l2 = ListNode(2)
        l3 = ListNode(3)
        l1.next = l2
        l2.next = l3
        head = l1
        while head:
            print(head.val)
            head = head.next
        r = self.reverseList(l1)
        head = r
        while head:
            print(head.val)
            head = head.next


s = Solution()
s.run()
