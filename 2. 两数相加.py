# Definition for singly-linked list.
from leetcode.list_node import ListNode as L


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


class Solution(object):
    @staticmethod
    def addTwoNumbers(l1, l2):
        ln1, ln2 = l1, l2  # l1留着返回
        carry = 0  # 进位值
        p = None  # 每位相加和
        while True:
            p = ln1.val + ln2.val + carry  # 每位相加并加上进位值
            if p >= 10:  # 判定是否需要进位
                carry = p // 10
                p = p % 10
            else:
                carry = 0
            ln1.val = p

            if ln1.next or ln2.next:
                if not ln2.next:  # 如果下一个为空赋值0
                    ln2.next = ListNode(0)
                if not ln1.next:  # 如果下一个为空赋值0
                    ln1.next = ListNode(0)
                ln1 = ln1.next
                ln2 = ln2.next
            else:
                break
        if carry:  # 加上最后一个进位
            ln1.next = ListNode(carry)
        return l1

    @staticmethod
    def addTwoNumbers2(l1, l2):
        tmp = ListNode(0)
        head = tmp
        carry, p, n1, n2 = 0, 0, 0, 0
        while l1 or l2 or carry:
            if l1:
                n1 = l1.val
                l1 = l1.next
            else:
                n1 = 0
            if l2:
                n2 = l2.val
                l2 = l2.next
            else:
                n2 = 0
            p = n1 + n2 + carry
            head.next = ListNode(p % 10)
            head = head.next
            carry = p // 10
        return tmp.next


if __name__ == '__main__':
    l1 = L()
    l1.append(2)
    l1.append(3)
    l1.append(4)
    print(l1)
    l2 = L()
    l2.append(5)
    l2.append(6)
    l2.append(4)
    print(l2)
    s = Solution()
    ln1 = l1.head
    ln2 = l2.head
    r = s.addTwoNumbers2(ln1, ln2)
    print(r)
