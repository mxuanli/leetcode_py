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
        left = True
        while q:
            tmp = list()
            len_q = len(q)  # 先在这确认q当前的长度
            for _ in range(len_q):
                t = q.pop(0)
                if left:
                    tmp.append(t.val)  # 如果left为true，正序添加值到临时列表
                else:
                    tmp.insert(0, t.val)  # 如果left为false，倒序添加值到临时列表
                # 添加子节点到辅助队列里
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
            left = False if left else True
            r.append(tmp)
        return r

    def run(self):
        root = TreeNode(1)
        t1 = TreeNode(2)
        t2 = TreeNode(3)
        t3 = TreeNode(4)
        t4 = TreeNode(5)
        root.left = t1
        root.right = t2
        t1.left = t3
        t2.right = t4
        r = self.zigzagLevelOrder(root)
        print(r)


s = Solution()
s.run()
