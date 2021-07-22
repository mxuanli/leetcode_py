"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        r = Node(0)  # 结果
        head1 = head  # 原链表
        head2 = r  # 新链表
        dict_node = dict()
        # 复制原链表节点
        while head1:
            dict_node[head1] = Node(head1.val)
            head1 = head1.next
        # 组成新链表
        for k, v in dict_node.items():
            head2.next = v
            head2.next.next = dict_node[k.next] if k.next else None
            head2.next.random = dict_node[k.random] if k.random else None
            head2 = head2.next
        return r.next
