# Definition for a binary tree node.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 广度优先遍历
        if not root:
            return list()
        r = list()
        q = [root]
        while q:
            tmp = list()
            len_q = len(q)  # 先在这确认q当前的长度
            for _ in range(len_q):
                t = q.pop(0)
                tmp.append(t.val)  # 添加值到临时列表
                # 从左到右添加子节点到辅助队列里
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            r.append(tmp)
        return r



