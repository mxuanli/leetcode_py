"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def __init__(self):
        self.nnl = None

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next:
            return head
        head_f = ListNode(0)
        head_f.next = head
        head = head_f
        n = n - m
        tmp = ListNode(0)
        while m > 0:
            tmp = head
            head = head.next
            m -= 1
        head_1 = head
        pre = None
        while head and n >= 0:
            nnl = head.next
            head.next = pre
            pre = head
            head = nnl
            n -= 1
        tmp.next = pre
        head_1.next = head
        return head_f.next

    def reverseBetween2(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == 1:
            return self.foo(head, n)
        head.next = self.reverseBetween2(head.next, m-1, n-1)
        return head

    def foo(self, head: ListNode, n: int):
        if n == 1:
            self.nnl = head.next
            return head
        last = self.foo(head.next, n-1)
        head.next.next = head
        head.next = self.nnl
        return last

    def run(self):
        l1 = ListNode(1)
        l2 = ListNode(2)
        l3 = ListNode(3)
        l4 = ListNode(4)
        l5 = ListNode(5)
        l1.next = l2
        l2.next = l3
        l3.next = l4
        l4.next = l5
        head = l1
        while head is not None:
            print(head.val)
            head = head.next
        m = 2
        n = 4
        print("-----")
        r = self.reverseBetween(l1, m, n)
        # r = self.foo(l1, 3)
        head = r
        while head is not None:
            print(head.val)
            head = head.next


class Solution2:

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or not head.next:
            return head
        head_f = ListNode(0)
        head_f.next = head
        head = head_f
        head_left = ListNode(0)
        for i in range(left):
            head_left = head
            head = head.next
        head1 = head
        pre = None
        for i in range(left, right + 1):
            tmp = head.next  # 临时变量指向head下一个
            head.next = pre  # head的下一个指向上一个
            pre = head  # pre指向当前值
            head = tmp  # head指向下一个值
        head_left.next = pre  # 链接未反转之前的最后一个值和反转的最后一个值
        head1.next = head  # 链接反转的第一个值和反转之后的第一个值
        return head_f.next

    def run(self):
        l1 = ListNode(1)
        l2 = ListNode(2)
        l3 = ListNode(3)
        l4 = ListNode(4)
        l5 = ListNode(5)
        l1.next = l2
        l2.next = l3
        l3.next = l4
        l4.next = l5
        head = l1
        while head is not None:
            print(head.val)
            head = head.next
        m = 2
        n = 4
        print("-----")
        r = self.reverseBetween(l1, m, n)
        # r = self.foo(l1, 3)
        head = r
        while head is not None:
            print(head.val)
            head = head.next


s = Solution2()
s.run()
