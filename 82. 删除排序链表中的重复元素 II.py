

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def deleteDuplicates(self, head):
        if not head:
            return head
        tmp = ListNode(0)
        tmp.next = head
        head = tmp
        while head.next and head.next.next:
            if head.next.val == head.next.next.val:
                val = head.next.val
                while head.next and head.next.val == val:
                    head.next = head.next.next
            else:
                head = head.next
        return tmp.next

    def deleteDuplicates2(self, head):
        if head is None:
            return head
        tmp = ListNode(0)
        tmp.next = head
        a = tmp
        b = head
        while b is not None and b.next is not None:
            if a.next.val == b.next.val:
                while b and b.next and a.next.val == b.next.val:
                    b = b.next
                a.next = b.next
                b = b.next
            else:
                a = a.next
                b = b.next
        return tmp.next

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
