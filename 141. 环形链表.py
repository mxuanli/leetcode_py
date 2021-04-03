"""
给定一个链表，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 true 。 否则，返回 false 。

 

进阶：

你能用 O(1)（即，常量）内存解决此问题吗？
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def hasCycle2(self, head: ListNode) -> bool:
        if not head:
            return False
        left = head
        right = head.next
        while right and right.next:
            if left == right:
                return True
            left = left.next
            right = right.next.next
        return False

    def hasCycle(self, head: ListNode) -> bool:
        while head and head.next:
            if head == head.next:
                return True
            nnl = head.next
            head.next = head
            head = nnl
        return False

    def run(self):
        l1 = ListNode(1)
        l2 = ListNode(2)
        l3 = ListNode(3)
        l1.next = l2
        l2.next = l3
        head = l1
        # while head:
        #     print(head.val)
        #     head = head.next
        r = self.hasCycle(l1)
        print(r)

s = Solution()
s.run()
