# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        head1 = l1
        head2 = l2
        val_list = list()
        while head1 is not None:
            val = head1.val
            head1 = head1.next
            val_list.append(val)
        while head2 is not None:
            val = head2.val
            head2 = head2.next
            val_list.append(val)
        if not val_list:
            return None
        val_list.sort()
        head = ListNode()
        tmp = ListNode()
        tmp.next = head
        for i, val in enumerate(val_list):
            head.val = val
            if i < len(val_list) - 1:
                head.next = ListNode()
                head = head.next
        return tmp.next

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

        ll1 = ListNode()
        ll2 = ListNode()
        ll3 = ListNode()
        ll4 = ListNode()
        ll1.val = 5
        ll2.val = 6
        ll3.val = 7
        ll4.val = 8
        ll1.next = ll2
        ll2.next = ll3
        ll3.next = ll4

        r = self.mergeTwoLists(l1, ll1)
        head = r
        while head is not None:
            print(head.val)
            head = head.next


s = Solution()
s.run()


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        r = ListNode()
        head = r
        while l1 and l2:
            # 取出来两个链表中较小的值，放在新的链表里
            if l1.val <= l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next
            head.next = node
            head = head.next
        # 剩下的值接在新链表里
        if l1:
            head.next = l1
        if l2:
            head.next = l2
        return r.next
