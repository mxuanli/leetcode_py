
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def deleteDuplicates(self, head):
        if head is None:
            return head
        tmp = head
        while tmp is not None:
            while tmp.next is not None and tmp.val == tmp.next.val:
                tmp.next = tmp.next.next
            tmp = tmp.next
        return head

    def run(self):
        l1 = ListNode(1)
        l2 = ListNode(1)
        l3 = ListNode(2)
        l1.next = l2
        l2.next = l3
        head = l1
        while head is not None:
            print(head.val)
            head = head.next
        r = self.deleteDuplicates(l1)
        head = r
        while head is not None:
            print(head.val)
            head = head.next


s = Solution()
s.run()
