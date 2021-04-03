# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def partition(self, head: ListNode, x: int) -> ListNode:
        # 两个链表，比较大小后合并
        small = small_pre = ListNode(0)
        big = big_pre = ListNode(0)
        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                big.next = head
                big = big.next
            head = head.next
        small.next = big_pre.next
        big.next = None
        return small_pre.next

    def partition1(self, head: ListNode, x: int) -> ListNode:
        big, small = list(), list()
        while head:
            if head.val < x:
                small.append(head)
            else:
                big.append(head)
            head = head.next
        head = ListNode(0)
        head_pre = head
        for node in small + big:
            head.next = node
            head = head.next
        head.next = None
        return head_pre.next


    def run(self):
        a1 = ListNode(1)
        a2 = ListNode(4)
        a3 = ListNode(3)
        a4 = ListNode(2)
        a5 = ListNode(5)
        a6 = ListNode(2)
        a1.next = a2
        a2.next = a3
        a3.next = a4
        a4.next = a5
        a5.next = a6
        x = 3
        r = self.partition1(a1, x)
        while r:
            print(r.val)
            r = r.next


s = Solution()
s.run()
