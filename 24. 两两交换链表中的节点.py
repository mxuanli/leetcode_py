# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def swapPairs(self, head: ListNode) -> ListNode:
        return self.foo(head)

    def foo(self, head: ListNode):
        if head is None or head.next is None:
            return head
        n_n_l = head.next.next
        n_l = head.next
        n_l.next = head
        head.next = self.foo(n_n_l)
        return n_l

    def run(self):
        l1 = ListNode()
        l2 = ListNode()
        l3 = ListNode()
        l4 = ListNode()
        l1.val = 1
        l2.val = 2
        l3.val = 3
        l4.val = 4
        l1.next = l2
        l2.next = l3
        l3.next = l4
        head = l1
        while head is not None:
            print(head.val)
            head = head.next
        r = self.swapPairs(l1)
        head = r
        while head is not None:
            print(head.val)
            head = head.next


s = Solution()
s.run()
